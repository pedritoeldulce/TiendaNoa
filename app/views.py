# arquitectura MVC
from flask import Blueprint, render_template

page = Blueprint('page', __name__)


@page.route('/')
def index():
    return render_template("index.html")


@page.app_errorhandler(404) # manejador de error, proporcionado por Bluesprint
def page_not_found(error):
    return render_template('errors/404.html'), 404


@page.route('/login')
def login():
    return render_template('auth/login.html')