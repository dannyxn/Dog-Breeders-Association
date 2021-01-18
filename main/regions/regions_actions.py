from flask import render_template, redirect, url_for, flash
from .sql import *
from ..utils import handle_postgres_error


def handle_add(request, cursor, conn):
    if request.method == 'POST':
        try:
            region_name_to_add = request.form.get('region_name_to_add')
            cursor.execute(GET_LATEST_ID)
            new_id = cursor.fetchall()[0][0] + 1
            cursor.execute(ADD_REGION.format(new_id, region_name_to_add))
            conn.commit()
            return redirect(url_for('browser.regions'))
        except Exception as err:
            return handle_postgres_error(err, cursor, conn, 'editor.regions')

def handle_delete(request, cursor, conn):
    if request.method == 'POST':
        try:
            region_id_to_delete = request.form['region_id_to_delete']
            cursor.execute(POSSIBLE_TO_DELETE_REGION.format(region_id_to_delete))
            possible_to_delete_region = cursor.fetchall()
            if possible_to_delete_region[0][0]:
                cursor.execute(DELETE_REGION.format(region_id_to_delete))
                conn.commit()
            else:
                flash("Nie można usunąć regionu o id = {}, ponieważ referencję"
                      " do tego klucza znaleziono w innych tabelach".format(region_id_to_delete))
            return redirect(url_for('browser.regions'))
        except Exception as err:
            return handle_postgres_error(err, cursor, conn, 'editor.regions')

def handle_edit(request, cursor, conn):
    if request.method == 'POST':
        try:
            region_name_to_set = request.form.get('region_name_to_set')
            region_id_to_edit = request.form['region_id_to_edit']
            cursor.execute(UPDATE_REGION.format(region_name_to_set, region_id_to_edit))
            conn.commit()
            return redirect(url_for('browser.regions'))
        except Exception as err:
            return handle_postgres_error(err, cursor, conn, 'editor.regions')

def handle_search(request, cursor):
    try:
        if request.method == 'GET':
            region_name = request.args.get('region_name')
            query = SEARCH_REGIONS
            built_query = ""
            if region_name:
                built_query += " nazwa = '{}'".format(region_name)

            if built_query == "":
                cursor.execute(SEARCH_REGIONS)
            else:
                cursor.execute(query + built_query)

            results = cursor.fetchall()
            return render_template('browser/regions.html', regions=results)
    except Exception as err:
        return handle_postgres_error(err, cursor, conn, 'browser.regions')