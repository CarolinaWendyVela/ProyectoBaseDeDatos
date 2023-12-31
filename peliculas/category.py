from flask import (Blueprint, render_template)
from werkzeug.exceptions import abort

from peliculas.db import get_db

bp = Blueprint('category', __name__, url_prefix="/category/")

def listaDeCategory():
    db = get_db()
    category = db.execute(
        """SELECT name FROM category ORDER BY name ASC;"""

    ).fetchall()
    return category


@bp.route('/')
def index():
    db = get_db()
    categorias = db.execute(
        """SELECT name FROM category ORDER BY name ASC;"""

    ).fetchall()
    return render_template('category/index.html', categorias=categorias)


@bp.route('/detalle/<int:id>')
def detalle(id):
    db = get_db()
    categoria = db.execute(
    """SELECT first_name, last_name 
        FROM  categoria
        WHERE categoria_id = ?
        ORDER BY first_name;""",
        (id,)

    ).fetchall()
    return render_template('actor/detalle.html', categoria=categoria)
