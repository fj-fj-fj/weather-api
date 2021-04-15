from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app(app: Flask) -> None:
    db.init_app(app)


def recreate(db):
    for command in (db.drop_all, db.create_all, db.session.commit):
        command()
