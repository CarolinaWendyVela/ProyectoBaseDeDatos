from flask import (Blueprint, render_template)
from peliculas.db import get_db

bp = Blueprint('language', __name__, url_prefix="/language/")


def listaDeLanguage():
    db = get_db()
    language = db.execute(
        "SELECT name FROM language ORDER BY name ASC;"

    ).fetchall()
    return language

@bp.route('/')
def index():
    language = listaDeLanguage()
    return render_template('language/index.html', language=language)
