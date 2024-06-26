"""Module providing a function printing python version."""

from os import environ

from flask import Flask
from waitress import serve

from controllers.admin_controller import admin_controller
from controllers.history_controller import history_controller
from controllers.translate_controller import translate_controller

app = Flask(__name__)
app.template_folder = "views/templates"
app.static_folder = "views/static"

app.register_blueprint(admin_controller, url_prefix="/admin")
app.register_blueprint(translate_controller, url_prefix="/")
app.register_blueprint(history_controller, url_prefix="/history")


def start_server(host="0.0.0.0", port=8000):
    """Function printing python version."""
    if environ.get("FLASK_ENV") != "production":
        return app.run(debug=True, host=host, port=port)
    else:
        serve(app, host=host, port=port)


if __name__ == "__main__":
    start_server()
