from flask import Flask, request, render_template, abort, jsonify # noqa
from models import Employee, EmployeeSchema, APIAuth, db, ma # noqa
from dotenv import load_dotenv # noqa
from functools import wraps
import os
import uuid


load_dotenv()
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
ma.init_app(app)

employee_schema = EmployeeSchema()
employees_schema = EmployeeSchema(many=True)


# Creates database with one dummy record
def setup_database(app):
    with app.app_context():
        db.create_all()
        if (not Employee.query.first()):
            employee = Employee("Vansh Jain", "Mumbai", "India")
            db.session.add(employee)
            db.session.commit()


# Generate API Keys
def generate_api_key():
    return str(uuid.uuid4())


# Get matching API Key
def get_api_key(key):
    return APIAuth.query.get(key)


# Verify API Key
def verify_api_key(key):
    if key is None:
        return False

    api_key = get_api_key(key)

    if api_key is None:
        return False
    elif api_key.key == key:
        return True

    return False


# Function Decorator to Require API Key
def require_app_key(fn):
    @wraps(fn)
    def decorated(*args, **kwargs):
        if verify_api_key(request.args.get('key')):
            return fn(*args, **kwargs)
        else:
            abort(401)

        return decorated


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


# Custom 404 Page
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


# Custom 405 Page
@app.errorhandler(405)
def method_not_allowed(e):
    allowed_methods = request.routing_exception.valid_methods
    return render_template("405.html", methods=allowed_methods)


if __name__ == '__main__':
    setup_database(app)
    app.run()
