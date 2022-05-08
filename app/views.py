# arquitectura MVC
from flask import Blueprint, render_template, request, redirect, url_for

page = Blueprint('page', __name__)


@page.route('/')
def index():
    return render_template("index.html")


@page.app_errorhandler(404) # manejador de error, proporcionado por Bluesprint
def page_not_found(error):
    return render_template('errors/404.html'), 404


@page.route('/login', methods=['POST', 'GET'])
def login():

    if request.method == 'POST':
        print(request.form['usuario'])
        print(request.form['password'])

        if request.form['usuario'] == 'admin' and request.form['password'] == '12345':
            return redirect(url_for('page.index'))
        else:
            return render_template('auth/login.html')

    return render_template('auth/login.html')


@page.route('/list-users')
def list_users():

    from .models import User

    try:
        users = User.users_list()
    except Exception as ex:
        print(ex)

    return render_template("list_user.html", users=users)