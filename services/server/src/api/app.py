# services/src/api/app.py

from flask_restplus import Namespace, Resource

app_namespace = Namespace("app")


class App(Resource):
    def get(self):
        return {"status": "success", "message": "app started"}


app_namespace.add_resource(App, "")
