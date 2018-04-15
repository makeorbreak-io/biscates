from app import db
from sqlalchemy import Column, DateTime, ForeignKey, UniqueConstraint, func
import enum, datetime


class Type(enum.Enum):
    Costuraria = 'Costuraria'
    Electricidade = 'Electricidade'
    Canalizações = 'Canalizações'
    Jardinagem = 'Jardinagem'
    Limpeza = 'Limpeza'
    Carpintaria = 'Carpintaria'
    Pintura = 'Pintura'
    Serralharia = 'Serralharia'


class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    photo = db.Column(db.String())
    address = db.Column(db.String())
    contact = db.Column(db.String())
    certified = db.Column(db.Boolean())
    created_at = db.Column(DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(DateTime(timezone=True), onupdate=func.now())
    description = db.Column(db.String())

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return '<id {} name {} email {} photo {} address {} contact {} certified {} description {}>'.format(self.id, self.email, self.photo, self.address, self.contact, self.certified, self.description)


class Tasks(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    location = db.Column(db.String(), nullable=False)
    price = db.Column(db.Float, nullable = False)
    description = db.Column(db.String())
    user = db.Column(ForeignKey("users.id"), nullable=False)
    type = db.Column(db.Enum(Type))
    approved = db.Column(db.Boolean(), default=False)
    created_at = db.Column(DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(DateTime(timezone=True), onupdate=func.now())

    def __init__(self, title, location, price, description, user, type):
        self.title = title
        self.location = location
        self.price = price
        self.description = description
        self.user = user
        self.type = type

    def __repr__(self):
        return '<id {} title {} type {} approved {} user {} location {} description {}>'.format(self.id, self.title, self.type, self.approved, self.user, self.location, self.description)


class Ratings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Integer, nullable=False)
    from_user = db.Column(ForeignKey("users.id"), nullable=False)
    to_user = db.Column(ForeignKey("users.id"), nullable=False)
    task = db.Column(ForeignKey("tasks.id"), nullable=False)
    __table_args__ = (UniqueConstraint('from_user', 'to_user', 'task', name='unique_user_rating'),)

    def __init__(self, value, from_user, to_user, task):
        self.value = value
        self.from_user = from_user
        self.to_user = to_user
        self.task = task

    def __repr__(self):
        return '<id {} value {}>'.format(self.id, self.value)


class Proposals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(ForeignKey("users.id"), nullable=False)
    offer = db.Column(db.Float, nullable=False)
    description = db.Column(db.String())
    accepted = db.Column(db.Boolean(), default=False)
    task = db.Column(ForeignKey("tasks.id"), nullable=False)

    def __init__(self, user, offer, description, accepted, task):
        self.user = user
        self.offer = offer
        self.description = description
        self.accepted = accepted
        self.task = task

    def __repr__(self):
        return '<id {} user {} offer {} description {} accepted {} task {}>'.format(self.id, self.user, self.offer, self.description, self.accepted, self.task)
