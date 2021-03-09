from flask import Flask


def create_app():
    app = Flask(__name__)

    from .routes.v1 import api as api_v1
    app.register_blueprint(api_v1, url_prefix='/v1')

    return app