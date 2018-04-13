from app import db
from sqlalchemy import Column

class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    password = db.Column(db.String())
    photo = db.Column(db.String())
    address = db.Column(db.String())
    name = db.Column(db.Boolean())

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def __repr__(self):
        return '<id {}>'.format(self.id)
