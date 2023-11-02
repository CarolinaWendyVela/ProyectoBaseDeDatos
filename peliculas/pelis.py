from flask import (Blueprint, render_template, jsonify, url_for)
from werkzeug.exceptions import abort

from peliculas.db import get_db

bp = Blueprint('movie', __name__)
bp_api = Blueprint('api_pelis', __name__, url_prefix="/api/pelis/")


def listaDePelis():
    db = get_db()
    Pelis = db.execute(
       "SELECT film_id, title, release_year, description FROM film ORDER BY title ASC;"

    ).fetchall()
    return Pelis


@bp.route('/')
def index():
    movies = listaDePelis()
    return render_template('movie/index.html', movies=movies)


@bp_api.route('/')
def index_api():
    movies = listaDePelis()
    for movie in movies:
        movie["url"] = url_for("api_pelis.detalleApi", id=movie["film_id"], _external=True)
    return jsonify( movies=movies)


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

    actores = db.execute(
        """SELECT a.first_name, a.last_name, a.actor_id
FROM film_actor fa JOIN actor a ON a.actor_id = fa.actor_id
WHERE fa.film_id = ?;""",
        (id,)
    ).fetchall()
    return render_template('movie/detalle.html', peli=peli, actores=actores)


@bp_api.route('/detalle/<int:id>')
def detalleApi(id):
    db = get_db()
    pelis = db.execute(
        """SELECT f.title, f.release_year, f.description 
        FROM film f
        WHERE f.film_id = ?
        ORDER BY title ASC;""",
      (id,)
    ).fetchone()

    actores = db.execute(
        """SELECT a.first_name, a.last_name, a.actor_id
FROM film_actor fa JOIN actor a ON a.actor_id = fa.actor_id
WHERE fa.film_id = ?;""",
        (id,)
    ).fetchall()
    for actor in actores:
        actor["url"] = url_for("api_actor.detalleApi", id=actor["actor_id"], _external=True)    
    return jsonify(pelis=pelis, actores=actores)
