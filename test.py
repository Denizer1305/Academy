import datetime

from flask import Flask, render_template, make_response, url_for, redirect, request, session

app = Flask(__name__)
app.config['SECRET_KEY'] = "zheaurhneyrayrbieutsctrytetyurbtairtert"
app.permanent_session_lifetime = datetime.timedelta(days=10 )
menu = [
    {"title": "Main", "url": "/"}
]


@app.route("/")
def index():
    if "visits" in session:
        session["visits"] = session.get("visits") + 1
    else:
        session["visits"] = 1
    return f"<h1>Main page</h1> visits {session['visits']}"
    # data = '{"name": "John Smith", "hometown": {"name": "New York", "id": "123"}}'
    # res = make_response(data)
    # res.headers["Content-Type"] = "application/json"
    # return res
    # audio = None
    # with app.open_resource(app.root_path + "/static/audio/1.mp3", mode="rb") as f:
    #     audio = f.read()
    #
    # if audio is None:
    #     return "None image"
    #
    # res = make_response(audio)
    # res.headers["Content-Type"] = 'audio/mp4'
    # return res

    # contex = render_template("index.html", menu=menu, posts=[])
    # res = make_response(contex)
    # res.headers["Content-Type"] = "text/plain"
    # return res
# @app.route("/transfer")
# def transfer():
#     return redirect(url_for("index")), 301
#
#
# @app.before_first_request
# def before_first_request():
#     print("before_first_request")
#
#
# @app.before_request
# def before_request():
#     print("before_request")
#
#
# @app.after_request
# def after_request(response):
#     print("after_request")
#     return response
#
#
# @app.teardown_request
# def teardown_request(response):
#     print("teardown_request")
#     return response


@app.route("/login")
def login():
    log = ""
    if request.cookies.get("logged"):
        log = request.cookies.get("logged")

    res = make_response(f"<h1> Форма авторизации </h1> logged: {log}")
    res.set_cookie("logged", "yes", 30*24*3600)
    return res


@app.route("/logout")
def logout():
    res = make_response("Вы больше не авторизованы")
    res.set_cookie("logged", "")
    return res


if __name__ == "__main__":
    app.run(debug=True)
