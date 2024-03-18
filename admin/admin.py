from flask import Blueprint, render_template

admin = Blueprint('admin', __name__, template_folder='templates', static_folder="static")
menu = [{'url': '.index', 'title': 'Панель'}, {'url': '.logout', 'title': 'Выйти'}]


@admin.route("/")
def index():
    return render_template("admin/base.html", title="Главная", menu=menu)


@admin.route('/login', methods=["POST", "GET"])
def login():
    return render_template("admin/login.html", title="Войти")


@admin.route('/logout')
def logout():
    pass