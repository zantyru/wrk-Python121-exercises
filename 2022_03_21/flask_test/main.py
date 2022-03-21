from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, world. <a href='/main'>На главную</a></p>"


@app.route("/test")
def test():
    return "<p>Это тест.</p>"


@app.route("/user/<name>")
def user_name(name):
    return f"Привет, {name}"


@app.route("/main")
@app.route("/main/<message>")
def main_page(message=None):
    return render_template("index.html", message_text=message)
