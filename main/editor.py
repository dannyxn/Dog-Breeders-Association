import psycopg2

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('editor', __name__, url_prefix='/edit')


@bp.route('/kennels')
def kennels():
    return render_template('editor/kennels.html')

@bp.route('/dogs')
def dogs():
    return render_template('editor/dogs.html')

@bp.route('/regions')
def regions():
    return render_template('editor/regions.html')

@bp.route('/breeds')
def breeds():
    return render_template('editor/breeds.html')


@bp.route('/litters')
def litters():
    return render_template('editor/litters.html')

@bp.route('/exams')
def exams():
    return render_template('editor/exams.html')
