from flask import Flask
from .views import page


# Singleton
app = Flask(__name__)


def create_app(config):
    app.register_blueprint(page)  # pasamos las rutas al servidor
    app.config.from_object(config)

    return app
