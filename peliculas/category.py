from flask import (Blueprint, flash, g, redirect, render_template, request, url_for)
from werkzeug.exceptions import abort

from flaskr.db import get_db

bp = Blueprint('category', __name__, url_prefix="/category/")

@bp.route('/')
def index():
    db = get_db()
    categorias = db.execute(
        """SELECT name FROM category ORDER BY name ASC;"""

    ).fetchall()
    return render_template('category/index.html', categorias=categorias)

