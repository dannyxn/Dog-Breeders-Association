import psycopg2

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('browser', __name__, url_prefix='/browse')

host = "127.0.0.1"
port = "5432"
dbname = "postgres"
user = "postgres"
pw = "postgres"
conn = psycopg2.connect(host=host, port=port, dbname=dbname, user=user, password=pw)
cursor = conn.cursor()
cursor.execute("SET SEARCH_PATH TO zwiazek")



@bp.route('/breeders')
def breeders():
    return render_template('browser/breeders.html')


@bp.route('/kennels')
def kennels():
    return render_template('browser/kennels_list.html')


@bp.route('/dogs')
def dogs():
    return render_template('browser/dogs.html')

@bp.route('/regions')
def regions():
    cursor.execute("SELECT * FROM Region")
    regions = cursor.fetchall()

    return render_template('browser/regions.html', regions=regions)


@bp.route('/breeds')
def breeds():
    return render_template('browser/breeds.html')


@bp.route('/litters')
def litters():
    return render_template('browser/litters.html')


@bp.route('/exams')
def exams():
    return render_template('browser/exams.html')

@bp.route('/employees')
def employees():
    return render_template('employees.html')
