from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import config


db = SQLAlchemy()
migrate = Migrate()
from DoList.DoList.models import *


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    db.init_app(app)
    migrate.init_app(app, db)
    blueprint_registration(app)
    return app


def blueprint_registration(app):
    pass

