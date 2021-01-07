import psycopg2

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('breeder', __name__, url_prefix='/breeder')

host = "127.0.0.1"
port = "5432"
dbname = "postgres"
user = "postgres"
pw = "postgres"
conn = psycopg2.connect(host=host, port=port, dbname=dbname, user=user, password=pw)
cursor = conn.cursor()
cursor.execute("SET SEARCH_PATH TO zwiazek")


@bp.route('/')
def index():
    return render_template('breeder/breeder.html')


@bp.route('/kennels')
def kennels():
    return render_template('breeder/kennels_list.html')


@bp.route('/dogs')
def dogs():
    return render_template('breeder/dogs.html')


@bp.route('/regions')
def regions():
    cursor.execute("SELECT * FROM Region")
    regions = cursor.fetchall()

    return render_template('breeder/regions.html', regions=regions)


@bp.route('/breeds')
def breeds():
    return render_template('breeder/breeds.html')


@bp.route('/litters')
def litters():
    return render_template('breeder/litters.html')


@bp.route('/exams')
def exams():
    return render_template('breeder/exams.html')


@bp.route('/employees')
def employees():
    return render_template('breeder/employees.html')
