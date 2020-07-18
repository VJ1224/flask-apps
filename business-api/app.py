from flask import Flask, escape, request, render_template, jsonify, abort
import sqlite3
import setup

app = Flask(__name__)
setup.main()

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

@app.route('/')
def home():
    name = request.args.get("name", "World")
    return render_template("index.html",name=name, url=request.url_root)

@app.route('/employees/all', methods=['GET'])
def employees_all():
    sql_connect = sqlite3.connect('business.db')
    sql_connect.row_factory = dict_factory
    cursor = sql_connect.cursor()

    query = "SELECT * FROM employees"
    results = cursor.execute(query).fetchall()

    return jsonify(results)

@app.route('/employees', methods = ['GET'])
def employee_filter():
    query_parameters = request.args
    query = "SELECT * FROM employees WHERE"
    id = query_parameters.get('id')
    name = query_parameters.get('name')
    city = query_parameters.get('city')
    country = query_parameters.get('country')
    to_filter = []

    if id:
        query += ' id=? AND'
        to_filter.append(id)
    if name:
        query += ' name=? AND'
        to_filter.append(name)
    if city:
        query += ' city=? AND'
        to_filter.append(city)
    if country:
        query += ' country=? AND'
        to_filter.append(country)
    if not (id or name or city or country):
        abort(404)

    query = query[:-4] + ';'

    sql_connect = sqlite3.connect('business.db')
    sql_connect.row_factory = dict_factory
    cursor = sql_connect.cursor()

    results = cursor.execute(query, to_filter).fetchall()

    return jsonify(results)

if __name__ == '__main__':
    app.run()
