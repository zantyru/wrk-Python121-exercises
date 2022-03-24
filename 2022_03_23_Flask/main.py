from pathlib import Path
from flask import Flask, render_template
import db


# Вычисляем рабочую директорию (где лежит это файл `main.py`) и задаём путь к файлу сохранения
WORK_DIR = Path(__file__).absolute().parent
DB_FILENAME = WORK_DIR / Path("numbers.txt")

# Создание экземпляра приложения Flask
app = Flask(__name__)

# Список чисел, который загружен из файла
list_of_integers = []


# *** Обработчики URL ***


@app.route("/")
def index():
    # Обратите внимание, как передаётся параметр `numbers` в шаблон
    # и как в шаблоне указана подстановка значений через `{{ n }}`
    return render_template("index.html", numbers=list_of_integers)


@app.route("/save/<number>")
def save(number=None):
    if number is not None:
        db.save(DB_FILENAME, number)
        return render_template("save_success.html")
    return render_template("save_fail.html")


@app.route("/load")
def load():
    global list_of_integers
    list_of_integers = db.load(DB_FILENAME)
    return render_template("load_success.html")
