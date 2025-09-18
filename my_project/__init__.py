from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists, create_database
from flask_jwt_extended import JWTManager
from config import Config
from flasgger import Swagger
import pymysql

from my_project.auth.route import register_routes
from my_project.additional_for_db.additional_for_db import create_triggers, create_procedures, create_functions

db = SQLAlchemy()
pymysql.install_as_MySQLdb()

def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)

    jwt = JWTManager(app)
    swagger = Swagger(app)

    _init_db(app)
    register_routes(app)

    # create_triggers(app, db)
    # create_functions(app, db)
    # create_procedures(app, db)

    return app

def _init_db(app: Flask) -> None:
    db.init_app(app)

    if not database_exists(app.config["SQLALCHEMY_DATABASE_URI"]):
        create_database(app.config["SQLALCHEMY_DATABASE_URI"])

    import my_project.auth.domain
    with app.app_context():
        db.create_all()
