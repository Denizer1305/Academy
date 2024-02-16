from flask import Flask, render_template, request, flash, session, redirect, url_for, abort

app = Flask(__name__)


app.config["SECRET_KEY"] = "3SAgu6jDn-u3x6nIEPmf5lTS5"
menu = [{"name": "Главная", "url": "/"},
        {"name": "О нас", "url": "/about"},
        {"name": "Обратная связь", "url": "/contact"},
        # {"name": "Логин", "url": "/login"},
        ]


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", menu=menu, title="Главгая страница")


@app.route("/about")
def about():
    return render_template("about.html", menu=menu, title="Страница о компании")


@app.route("/profile/<username>")
def profile(username):
    if 'userLogged' not in session['userLogged'] != username:
        abort(401)
    return f"<h1> Пользователь: {username} </h1>"


@app.route('/contact', methods=["POST", "GET"])
def contact():
    if request.method == 'POST':
        if len(request.form['name']) >= 2:
            flash("Сообщение доставлено", category="success")
        else:
            flash("Ошибка!", category="error")
    return render_template("contact.html", menu=menu, title="Обратная связь")


@app.errorhandler(404)
def pageNotFound(error):
    return render_template("page404.html", menu=menu, title="Страница не найдена")


@app.route("/login", methods=["POST", "GET"])
def login():
    if 'userLogged' in session:
        return redirect(url_for('profile', username=session["userLogged"]))
    elif request.method == "POST":
        if request.form['name'] == 'Test' and request.form['psw'] == "123":
            session['userLogged'] = request.form['name']
            return redirect(url_for('profile', username=session["userLogged"]))
        else:
            flash("Ошибка авторизации!")
    return render_template("login.html", menu=menu, title="Логин")


if __name__ == "__main__":
    app.run(debug=True)
