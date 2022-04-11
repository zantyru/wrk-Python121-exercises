from pathlib import Path
from flask import Flask, render_template
import cloakroom as cr
import saver_loader


# Вычисляем рабочую директорию (где лежит это файл `main_2022_03_30.py`) и задаём путь к файлу сохранения
WORK_DIR = Path(__file__).absolute().parent
SAVE_FILENAME = WORK_DIR / Path("tags.sav")

# Создание экземпляра приложения Flask и всего остального
app = Flask(__name__)
cloakroom = cr.Cloakroom(100)


@app.route("/")
def index():
    saver_loader.load(SAVE_FILENAME, cloakroom)
    return render_template(
        "index.html",
        f_tags=cloakroom.get_free_tags(),
        a_tags=cloakroom.get_acquired_tags()
    )


@app.route("/acquire_free_tag")
def acquire_free_tag():
    tag = None
    error_message = ""

    try:
        tag = cloakroom.acquire_free_tag()
        saver_loader.save(SAVE_FILENAME, cloakroom)
    except cr.NotEnoughTagsError:
        error_message = "Нет свободных номерков!"

    return render_template(
        "index.html",
        f_tags=cloakroom.get_free_tags(),
        a_tags=cloakroom.get_acquired_tags(),
        acquired_tag=tag,
        error_message=error_message
    )


@app.route("/return_tag/<tag>")
def return_tag(tag=None):
    error_message = ""

    try:
        tag = int(tag)
        cloakroom.return_tag(tag)
        saver_loader.save(SAVE_FILENAME, cloakroom)
    except (TypeError, ValueError) as _:
        error_message = f"Передан не номерок: {tag}!"
    except cr.TagAlreadyReturnedError:
        error_message = "Номерок и так уже свободный!"
    except cr.UnknownTagError:
        error_message = f"Попытка вернут ошибочный номерок: {tag}!"

    return render_template(
        "index.html",
        f_tags=cloakroom.get_free_tags(),
        a_tags=cloakroom.get_acquired_tags(),
        returned_tag=tag,
        error_message=error_message
    )


@app.route("/is_tag_acquired/<tag>")
def is_tag_acquired(tag=None):
    ...


@app.route("/get_free_tags")
def get_free_tags():
    ...


@app.route("/get_acquired_tags")
def get_acquired_tags():
    ...