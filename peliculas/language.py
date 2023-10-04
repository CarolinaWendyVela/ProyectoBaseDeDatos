from flask import (Blueprint, flash, g, redirect, render_template, request, url_for)
from werkzeug.exceptions import abort

from flaskr.db import get_db

bp = Blueprint('language', __name__, url_prefix="/language/")

#5:
#RUTA DE LENGUAJES
@bp.route('/')
def index():
    db = get_db()
    languages = db.execute(
        "SELECT name FROM language ORDER BY name ASC;"
    ).fetchall()
    return render_template('language/index.html', languages=languages)


