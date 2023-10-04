from flask import (Blueprint, flash, g, redirect, render_template, request, url_for)
from werkzeug.exceptions import abort

from flaskr.db import get_db

bp = Blueprint('actor', __name__, url_prefix="/actor/")

@bp.route('/')
def index():
    db = get_db()
    actores = db.execute(
        """SELECT first_name, last_name FROM actor ORDER BY first_name;"""

    ).fetchall()
    return render_template('actor/index.html', actores=actores)
