# services/server/src/api/__init__.py

from flask_restplus import Api

from src.api.app import app_namespace

api = Api(version="1.0", title="usap directory API", doc="/doc/")

api.add_namespace(app_namespace, path="/app")
