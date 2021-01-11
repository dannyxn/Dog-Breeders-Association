import psycopg2
from .sql_mapping.listing import *
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
    cursor.execute(ALL_BREEDERS)
    breeders = cursor.fetchall()

    return render_template('browser/breeders.html', breeders=breeders)


@bp.route('/kennels')
def kennels():
    cursor.execute(ALL_KENNELS)
    kennels = cursor.fetchall()
    return render_template('browser/kennels_list.html', kennels=kennels)


@bp.route('/dogs')
def dogs():
    cursor.execute(ALL_DOGS)
    dogs = cursor.fetchall()
    return render_template('browser/dogs.html', dogs=dogs)

@bp.route('/regions')
def regions():
    cursor.execute(ALL_REGIONS)
    regions = cursor.fetchall()

    return render_template('browser/regions.html', regions=regions)


@bp.route('/breeds')
def breeds():
    cursor.execute(ALL_BREEDS)
    breeds = cursor.fetchall()

    return render_template('browser/breeds.html', breeds=breeds)

@bp.route('/litters')
def litters():
    cursor.execute(ALL_LITTERS)
    litters = cursor.fetchall()

    return render_template('browser/litters.html', litters=litters)

@bp.route('/exams')
def exams():
    cursor.execute(ALL_EXAMS)
    exams = cursor.fetchall()

    return render_template('browser/exams.html', exams=exams)

@bp.route('/employees')
def employees():
    cursor.execute(ALL_EMPLOYEES)
    employees = cursor.fetchall()

    return render_template('browser/employees.html', employees=employees)
