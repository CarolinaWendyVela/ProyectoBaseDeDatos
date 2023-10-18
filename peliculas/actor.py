from flask import (Blueprint, flash, g, redirect, render_template, request, url_for)
from werkzeug.exceptions import abort

from flaskr.db import get_db

bp = Blueprint('actor', __name__, url_prefix="/actor/")

@bp.route('/')
def index():
    db = get_db()
    actores = db.execute(
        """SELECT actor_id, first_name, last_name FROM actor ORDER BY first_name;"""

    ).fetchall()
    return render_template('actor/index.html', actores=actores)

@bp.route('/detalle/<int:id>')
def detalle(id):
    db = get_db()
    actor = db.execute(
       """SELECT actor_id, first_name, last_name 
          FROM actor 
          WHERE actor_id = ?
          ORDER BY first_name""",
          (id,)
    ).fetchone()
 
    peliculas = db.execute(
        """SELECT f.film_id, f.title, f.release_year, fa.actor_id 
            FROM film f JOIN film_actor fa ON f.film_id = fa.film_id 
           WHERE fa.actor_id = ? """,
        (id,)
    ).fetchall()

    return render_template('actor/detalle.html', actor=actor, peliculas=peliculas)
