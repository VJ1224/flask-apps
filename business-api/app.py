from flask import Flask, escape, request, render_template, jsonify
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
    return render_template("index.html",name=name, url=request.url_root)

@app.route('/employees/all', methods=['GET'])
def employees_all():
    sql_connect = sqlite3.connect('business.db')
    sql_connect.row_factory = dict_factory
    cursor = sql_connect.cursor()

    query = "SELECT * FROM employees"
    results = cursor.execute(query).fetchall()
    
    return jsonify(results)
