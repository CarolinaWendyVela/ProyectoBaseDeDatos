from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('movie', __name__)

@bp.route('/')
def index():
    db = get_db()
    movies = db.execute(
        "SELECT film_id, title, release_year, description FROM film ORDER BY title ASC;"
    ).fetchall()
    return render_template('movie/index.html', movies=movies)


@bp.route('/detalle/<int:id>')
def detalle(id):
    db = get_db()
    peli = db.execute(
        """SELECT f.title, f.release_year, f.description 
        FROM film f
        WHERE f.film_id = ?
        ORDER BY title ASC;""",
      (id,)
    ).fetchone()
    return render_template('movie/detalle.html', peli=peli)
