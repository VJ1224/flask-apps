from flask import Flask, request, render_template, abort, jsonify
from models import Employee, EmployeeSchema, db, ma
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
dbpath = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')

app.config['SQLALCHEMY_DATABASE_URI'] = dbpath
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db.init_app(app)
ma.init_app(app)

employee_schema = EmployeeSchema()
employees_schema = EmployeeSchema(many=True)


# Home
@app.route('/')
def home():
    name = request.args.get("name", "World")
    return render_template("index.html", name=name, url=request.url_root)


# Get All Employees
@app.route('/employees/all', methods=['GET'])
def employees_all():
    all_employees = Employee.query.all()
    result = employees_schema.dump(all_employees)

    return jsonify(result)


# Get Employee by ID
@app.route('/employees/<id>', methods=['GET'])
def employee_get(id):
    employee = Employee.query.get(id)

    return employee_schema.jsonify(employee)


# Add Employee
@app.route('/employees', methods=["POST"])
def employee_add():
    try:
        name = request.json['name']
        city = request.json['city']
        country = request.json['country']
    except KeyError:
        abort(404)

    new_employee = Employee(name, city, country)

    db.session.add(new_employee)
    db.session.commit()

    return employee_schema.jsonify(new_employee)


# Update Employee by ID
@app.route('/employees/<id>', methods=["PUT"])
def employee_update(id):
    employee = Employee.query.get(id)
    try:
        name = request.json['name']
        city = request.json['city']
        country = request.json['country']
    except KeyError:
        abort(404)

    employee.name = name
    employee.city = city
    employee.country = country

    db.session.commit()

    return employee_schema.jsonify(employee)


# Delete Employee by ID
@app.route('/employees/<id>', methods=["DELETE"])
def employee_delete(id):
    employee = Employee.query.get(id)

    db.session.delete(employee)
    db.session.commit()

    return employee_schema.jsonify(employee)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


@app.errorhandler(405)
def method_not_allowed(e):
    allowed_methods = request.routing_exception.valid_methods
    return render_template("405.html", methods=allowed_methods)


if __name__ == '__main__':
    app.run()
