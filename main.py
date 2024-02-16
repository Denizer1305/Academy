from flask import Flask, render_template, request, flash

app = Flask(__name__)


app.config["SECRET_KEY"] = "3SAgu6jDn-u3x6nIEPmf5lTS5"
menu = [{"name": "Главная", "url": "/"},
        {"name": "О нас", "url": "/about"},
        {"name": "Обратная связь", "url": "/contact"}, ]


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", menu=menu, title="Главгая страница")


@app.route("/about")
def about():
    return render_template("about.html", menu=menu, title="Страница о компании")


@app.route("/profile/<username>")
def profile(username):
    return f"Пользователь -- {username}"


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


if __name__ == "__main__":
    app.run(debug=True)
