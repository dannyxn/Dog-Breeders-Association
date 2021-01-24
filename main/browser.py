import psycopg2
from .breeders.sql import ALL_BREEDERS
from .breeds.sql import ALL_BREEDS
from .dogs.sql import ALL_DOGS
from .exams.sql import ALL_EXAMS
from .kennels.sql import ALL_KENNELS
from .litters.sql import ALL_LITTERS
from .regions.sql import ALL_REGIONS
from .breeders import breeders_actions
from .breeds import breeds_actions
from .dogs import dogs_actions
from .regions import regions_actions
from .litters import litters_actions
from .kennels import kennels_actions
from .exams import exams_actions
from .db import get_db
from flask import (
    Blueprint, render_template, request, session, g, redirect, url_for
)

ALL_EMPLOYEES = "SELECT * FROM Pracownik ORDER BY id"


bp = Blueprint('browser', __name__, url_prefix='/browse')


@bp.before_request
def before_request():
    get_db()
    if 'user_id' in session and 'user' in session:
        g.user = session['user']
        g.user_id = session['user_id']
    else:
        return redirect(url_for('auth.login'))


@bp.route('/breeders')
def breeders():
    g.cursor.execute(ALL_BREEDERS)
    all_breeders = g.cursor.fetchall()

    return render_template('browser/breeders.html', breeders=all_breeders)


@bp.route('/breeders/search')
def breeders_search():
    return breeders_actions.handle_search(request, g.cursor, g.conn)


@bp.route('/breeders/details/<int:id>')
def breeder_details(id):
    return breeders_actions.details(g.cursor, id, g.conn)


@bp.route('/kennels')
def kennels():
    g.cursor.execute(ALL_KENNELS)
    kennels = g.cursor.fetchall()
    return render_template('browser/kennels_list.html', kennels=kennels)


@bp.route('/kennels/search')
def kennels_search():
    return kennels_actions.handle_search(request, g.cursor, g.conn)


@bp.route('/dogs')
def dogs():
    g.cursor.execute(ALL_DOGS)
    dogs = g.cursor.fetchall()
    return render_template('browser/dogs.html', dogs=dogs)


@bp.route('/dogs/search')
def dogs_search():
    return dogs_actions.handle_search(request, g.cursor, g.conn)


@bp.route('/dogs/details/<int:id>')
def dog_details(id):
    return dogs_actions.details(request, g.cursor, id, g.conn)


@bp.route('/regions')
def regions():
    g.cursor.execute(ALL_REGIONS)
    regions = g.cursor.fetchall()

    return render_template('browser/regions.html', regions=regions)


@bp.route('/regions/search')
def regions_search():
    return regions_actions.handle_search(request, g.cursor, g.conn)


@bp.route('/breeds')
def breeds():
    g.cursor.execute(ALL_BREEDS)
    breeds = g.cursor.fetchall()

    return render_template('browser/breeds.html', breeds=breeds)


@bp.route('/breeds/search')
def breeds_search():
    return breeds_actions.handle_search(request, g.cursor, g.conn)


@bp.route('/litters')
def litters():
    g.cursor.execute(ALL_LITTERS)
    litters = g.cursor.fetchall()

    return render_template('browser/litters.html', litters=litters)


@bp.route('/litters/search')
def litters_search():
    return litters_actions.handle_search(request, g.cursor, g.conn)


@bp.route('/exams')
def exams():
    g.cursor.execute(ALL_EXAMS)
    exams = g.cursor.fetchall()

    return render_template('browser/exams.html', exams=exams)


@bp.route('/exams/search')
def exams_search():
    return exams_actions.handle_search(request, g.cursor, g.conn)


@bp.route('/employees')
def employees():
    g.cursor.execute(ALL_EMPLOYEES)
    employees = g.cursor.fetchall()

    return render_template('browser/employees.html', employees=employees)


@bp.route('/employees/search')
def employees_search():
    g.cursor.execute(ALL_EMPLOYEES)
    employees = g.cursor.fetchall()

    return render_template('browser/employees.html', employees=employees)
