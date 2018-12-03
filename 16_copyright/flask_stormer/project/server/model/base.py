from __future__ import unicode_literals
from project.server import db
from sqlalchemy.ext.declarative import as_declarative, declared_attr


class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()


class Timer(db.Model):
    __abstract__ = True

    created_time = db.Column(db.DateTime, default=db.func.now())
    updated_time = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
