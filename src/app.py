from flask import Flask
from .routes.api import api
from .routes.web import web


def create_app():
    app = Flask(__name__)
    app.register_blueprint(api)
    app.register_blueprint(web)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
