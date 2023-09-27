from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from peliculas.db import get_db

bp = Blueprint('blog', __name__)

@bp.route('/')
def index():
    db = get_db()
    posts = db.execute(
        """SELECT title, release_year, description
        FROM film
        ORDER BY title ASC;"""

    ).fetchall()
    return render_template('blog/index.html', posts=posts)
