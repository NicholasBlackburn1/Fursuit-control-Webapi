"""
app
"""
from utils import consolelog as logger
from api import routes
from pathlib import Path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger



def create_app():
    # creates the flask app
    logger.Warning("Creating flask app...")
    app = Flask(__name__, static_url_path="/files",
                static_folder="FursuitControl/static")

    logger.PipeLine_Ok("started flaskapp")

    logger.info("registered blueprints")

    app.config['SWAGGER'] = {
        "swagger_version": "2.0",
        "title": "Fursuit Control",
        "headers": [
            ('Access-Control-Allow-Origin', '*'),
            ('Access-Control-Allow-Methods', "GET, POST, PUT, DELETE, OPTIONS"),
            ('Access-Control-Allow-Credentials', "true"),
        ],
        "specs": [
            {
                "version": "1.0.0",
                "title": "Fursuit control",
                "endpoint": '/fursuit/api/docs',
                "description": 'This is the version 1 of our API',
                "route": '/fursuit/api/v1.0/',
            }
        ]
    }

    Swagger(app)
    app.register_blueprint(routes.apibp)
    logger.PipeLine_Ok("REGISTERED blueprints")


    return app