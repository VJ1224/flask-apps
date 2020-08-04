from flask_sqlalchemy import SQLAlchemy # noqa
from flask_marshmallow import Marshmallow # noqa

db = SQLAlchemy()
ma = Marshmallow()


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(100))
    country = db.Column(db.String(100))

    def __init__(self, name, city, country):
        self.name = name
        self.city = city
        self.country = country


class EmployeeSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'city', 'country')


class APIAuth(db.Model):
    key = db.Column(db.String, primary_key=True)

    def __init__(self, key):
        self.key = key
