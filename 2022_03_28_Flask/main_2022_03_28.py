from pathlib import Path
from flask import Flask, render_template
import cloakroom as cr


# Вычисляем рабочую директорию (где лежит это файл `main.py`) и задаём путь к файлу сохранения
WORK_DIR = Path(__file__).absolute().parent
SAVE_FILENAME = WORK_DIR / Path("tags.sav")

# Создание экземпляра приложения Flask и всего остального
app = Flask(__name__)
cloakroom = cr.Cloakroom(100)


def _get_all_tags():
    acquired_tags = cloakroom.get_acquired_tags()
    free_tags = cloakroom.get_free_tags()
    return [*acquired_tags, *free_tags]


@app.route("/")
def index():
    all_tags = _get_all_tags()
    return render_template(
        "index.html",
        all_tags=all_tags
    )


@app.route("/acquire_free_tag")
def acquire_free_tag():
    tag = None
    error_message = ""

    try:
        tag = cloakroom.acquire_free_tag()
    except cr.NotEnoughTagsError:
        error_message = "Нет свободных номерков!"

    all_tags = _get_all_tags()
    return render_template(
        "index.html",
        all_tags=all_tags,
        acquired_tag=tag,
        error_message=error_message
    )


@app.route("/return_tag/<tag>")
def return_tag(tag=None):
    ...


@app.route("/is_tag_acquired/<tag>")
def is_tag_acquired(tag=None):
    ...


@app.route("/get_free_tags")
def get_free_tags():
    ...


@app.route("/get_acquired_tags")
def get_acquired_tags():
    ...