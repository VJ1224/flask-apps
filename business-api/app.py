from flask import Flask, request, render_template, jsonify, abort
import sqlite3

app = Flask(__name__)


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route('/')
def home():
    name = request.args.get("name", "World")
    return render_template("index.html", name=name, url=request.url_root)


@app.route('/employees/all', methods=['GET'])
def employees_all():
    sql_connect = sqlite3.connect('business.db')
    sql_connect.row_factory = dict_factory
    cursor = sql_connect.cursor()

    query = "SELECT * FROM employees"
    results = cursor.execute(query).fetchall()
    sql_connect.close()

    return jsonify(results)


@app.route('/employees', methods=['GET'])
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
    sql_connect.close()

    return jsonify(results)


@app.route('/employees', methods=["POST"])
def employee_add():
    query_parameters = request.args
    query = "INSERT INTO employees (name, city, country) VALUES (?, ?, ?);"
    name = query_parameters.get('name')
    city = query_parameters.get('city')
    country = query_parameters.get('country')
    data = (name, city, country)

    if not (name or city or country):
        abort(404)

    sql_connect = sqlite3.connect('business.db')
    sql_connect.row_factory = dict_factory
    cursor = sql_connect.cursor()
    cursor.execute(query, data)

    id = cursor.lastrowid
    query = "SELECT * FROM employees WHERE id=?"
    result = cursor.execute(query, (id,)).fetchall()[0]

    sql_connect.commit()
    sql_connect.close()
    return jsonify(result)


@app.route('/employees', methods=["DELETE"])
def employee_delete():
    query = "SELECT * FROM employees WHERE id=?"
    query_parameters = request.args
    id = query_parameters.get('id')

    if not (id):
        abort(404)

    sql_connect = sqlite3.connect('business.db')
    sql_connect.row_factory = dict_factory
    cursor = sql_connect.cursor()
    result = cursor.execute(query, (id,)).fetchall()[0]

    query = "DELETE FROM employees WHERE id=?"
    cursor.execute(query, (id,))

    sql_connect.commit()
    sql_connect.close()
    return jsonify(result)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


@app.errorhandler(405)
def method_not_allowed(e):
    allowed_methods = request.routing_exception.valid_methods
    return render_template("405.html", methods=allowed_methods)


if __name__ == '__main__':
    app.run()
