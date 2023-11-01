from flask import (Blueprint, flash, g, redirect, render_template, request, url_for, jsonify)
from werkzeug.exceptions import abort

from peliculas.db import get_db

bp = Blueprint('language', __name__, url_prefix="/language/")
bpapi = Blueprint('api_language', __name__, url_prefix="/api/language/")


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


@bpapi.route('/')
def indexApi():
    language = listaDeLanguage()
    return jsonify(language=language)

@bp.route('/detalle/<int:id>')
def detalle(id):
    db = get_db()
    language = db.execute(
    """SELECT first_name, last_name 
        FROM  language
        WHERE language_id = ?
        ORDER BY first_name;""",
        (id,)

    ).fetchall()
    return render_template('actor/detalle.html', language=language)