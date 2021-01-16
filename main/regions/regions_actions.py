from flask import render_template, redirect, url_for
from .sql import *

def handle_add(request, cursor, conn):
    if request.method == 'POST':
        region_name_to_add = request.form.get('region_name_to_add')
        cursor.execute(GET_LATEST_ID)
        new_id = cursor.fetchall()[0][0] + 1
        cursor.execute(ADD_REGION.format(new_id, region_name_to_add))
        conn.commit()
        return redirect(url_for('browser.regions'))

def handle_delete(request, cursor, conn):
    if request.method == 'POST':
        region_id_to_delete = request.form['region_id_to_delete']
        cursor.execute(DELETE_REGION.format(region_id_to_delete))
        conn.commit()
        return redirect(url_for('browser.regions'))

def handle_edit(request, cursor, conn):
    if request.method == 'POST':
        region_name_to_set = request.form.get('region_name_to_set')
        region_id_to_edit = request.form['region_id_to_edit']
        cursor.execute(UPDATE_REGION.format(region_name_to_set, region_id_to_edit))
        conn.commit()
        return redirect(url_for('browser.regions'))

def handle_search(request, cursor):
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