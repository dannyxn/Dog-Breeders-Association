import psycopg2
from .breeders import breeders_actions
from .kennels import kennels_actions
from .dogs import dogs_actions
from .breeds import breeds_actions
from .regions import regions_actions
from .exams import exams_actions
from .litters import litters_actions

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('editor', __name__, url_prefix='/edit')
host = "127.0.0.1"
port = "5432"
dbname = "postgres"
user = "postgres"
pw = "postgres"
conn = psycopg2.connect(host=host, port=port, dbname=dbname, user=user, password=pw)
cursor = conn.cursor()
cursor.execute("SET SEARCH_PATH TO zwiazek")

@bp.before_request
def before_request():
    if 'user_id' in session and 'user' in session:
        g.user = session['user']
        g.user_id = session['user_id']
    else:
        return redirect(url_for('auth.login'))

@bp.route('/breeders')
def breeders():
    return render_template('editor/breeders.html')

@bp.route('/breeders/add', methods=['POST'])
def breeders_add():
    return breeders_actions.handle_add(request, cursor, conn)

@bp.route('/breeders/delete', methods=['POST'])
def breeders_delete():
    return breeders_actions.handle_delete(request, cursor, conn)

@bp.route('/breeders/edit', methods=['POST'])
def breeders_edit():
    return breeders_actions.handle_edit(request, cursor, conn)

@bp.route('/kennels')
def kennels():
    return render_template('editor/kennels.html')

@bp.route('/kennels/add', methods=['POST'])
def kennels_add():
    return kennels_actions.handle_add(request, cursor, conn)

@bp.route('/kennels/delete', methods=['POST'])
def kennels_delete():
    return kennels_actions.handle_delete(request, cursor, conn)

@bp.route('/kennels/edit', methods=['POST'])
def kennels_edit():
    return kennels_actions.handle_edit(request, cursor, conn)

@bp.route('/dogs')
def dogs():
    return render_template('editor/dogs.html')

@bp.route('/dogs/add', methods=['POST'])
def dogs_add():
    return dogs_actions.handle_add(request, cursor, conn)

@bp.route('/dogs/delete', methods=['POST'])
def dogs_delete():
    return dogs_actions.handle_delete(request, cursor, conn)

@bp.route('/dogs/edit', methods=['POST'])
def dogs_edit():
    return dogs_actions.handle_edit(request, cursor, conn)

@bp.route('/dogs/<int:id>/add_exam', methods=['POST'])
def dogs_add_passed_exam(id):
    return dogs_actions.handle_add_passed_exam(request, cursor, conn, id)

@bp.route('/regions', methods=['GET'])
def regions():
    return render_template('editor/regions.html')

@bp.route('/regions/add', methods=['POST'])
def regions_add():
    return regions_actions.handle_add(request, cursor, conn)

@bp.route('/regions/delete', methods=['POST'])
def regions_delete():
    return regions_actions.handle_delete(request, cursor, conn)

@bp.route('/regions/edit', methods=['POST'])
def regions_edit():
    return regions_actions.handle_edit(request, cursor, conn)

@bp.route('/breeds')
def breeds():
    return render_template('editor/breeds.html')

@bp.route('/breeds/add', methods=['POST'])
def breeds_add():
    return breeds_actions.handle_add(request, cursor, conn)

@bp.route('/breeds/delete', methods=['POST'])
def breeds_delete():
    return breeds_actions.handle_delete(request, cursor, conn)

@bp.route('/breeds/edit', methods=['POST'])
def breeds_edit():
    return breeds_actions.handle_edit(request, cursor, conn)

@bp.route('/litters')
def litters():
    return render_template('editor/litters.html')

@bp.route('/litters/add', methods=['POST'])
def litters_add():
    return litters_actions.handle_add(request, cursor, conn)

@bp.route('/litters/delete', methods=['POST'])
def litters_delete():
    return litters_actions.handle_delete(request, cursor, conn)

@bp.route('/litters/edit', methods=['POST'])
def litters_edit():
    return litters_actions.handle_edit(request, cursor, conn)


@bp.route('/exams')
def exams():
    return render_template('editor/exams.html')

@bp.route('/exams/add', methods=['POST'])
def exams_add():
    return exams_actions.handle_add(request, cursor, conn)

@bp.route('/exams/delete', methods=['POST'])
def exams_delete():
    return exams_actions.handle_delete(request, cursor, conn)

@bp.route('/exams/edit', methods=['POST'])
def exams_edit():
    return exams_actions.handle_edit(request, cursor, conn)