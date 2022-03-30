from pathlib import Path
from flask import Flask, render_template, request


WORK_DIR = Path(__file__).absolute().parent
DB_FILENAME = WORK_DIR / "logins.txt"


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("login.html", message=None, error=None)


@app.route("/register")
def register():
    return render_template("register.html", message=None, error=None)


# Подсказка userlogin = request.args.get("lgn")

