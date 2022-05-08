from flask import Flask
from .views import page
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy


csrf = CSRFProtect()
db = SQLAlchemy()


def create_app(config):
    # Singleton
    app = Flask(__name__)
    app.config.from_object(config)
    from app.models import User, Perfil, Product, Category

    app.register_blueprint(page)  # pasamos las rutas al servidor
    csrf.init_app(app)

    with app.app_context():
        db.init_app(app)
        db.create_all()

    return app
