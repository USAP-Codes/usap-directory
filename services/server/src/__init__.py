# services/server/src/__init__.py
import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_app():

    # instantiate app
    app = Flask(__name__)

    # set configs
    app.config.from_object(os.environ["APP_SETTINGS"])

    # register api to flask
    from src.api import api

    api.init_app(app)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {"app": app}

    return app


app = create_app()

db = SQLAlchemy(app)
