from flask import render_template, redirect, url_for
from .sql import *


def handle_add(request, cursor, conn):
    if request.method == 'POST':
        cursor.execute(GET_LATEST_ID)
        new_id = cursor.fetchall()[0][0] + 1
        kennel_name_to_add = request.form.get('kennel_name_to_add')
        breeder_id_to_add = request.form.get('breeder_id_to_add')
        region_id_to_add = request.form.get('region_id_to_add')
        cursor.execute(ADD_KENNEL.format(new_id, breeder_id_to_add, region_id_to_add, kennel_name_to_add))
        conn.commit()
        return redirect(url_for('browser.kennels'))


def handle_delete(request, cursor, conn):
    if request.method == 'POST':
        kennel_id_to_delete = request.form['kennel_id_to_delete']
        cursor.execute(DELETE_KENNEL.format(kennel_id_to_delete))
        conn.commit()
        return redirect(url_for('browser.kennels'))


def handle_edit(request, cursor, conn):
    if request.method == 'POST':
        kennel_id_to_edit = request.form.get('kennel_id_to_edit')
        kennel_name_to_edit = request.form.get('kennel_name_to_edit')
        breeder_id_to_edit = request.form.get('breeder_id_to_edit')
        region_id_to_edit = request.form.get('region_id_to_edit')
        cursor.execute(
            UPDATE_KENNEL.format(kennel_id_to_edit, breeder_id_to_edit, region_id_to_edit, kennel_name_to_edit))
        conn.commit()
        return redirect(url_for('browser.kennels'))

def handle_search(request, cursor):
    if request.method == 'GET':
        breeder_id = request.args.get('breeder_id')
        kennel_name = request.args.get('kennel_name')
        region_id = request.args.get('region_id')
        query = SEARCH_KENNELS
        any_condition_present = False
        built_query = ""
        if breeder_id:
            built_query += " id_wlasciciel = {}".format(breeder_id)
            any_condition_present = True

        if kennel_name:
            if any_condition_present:
                built_query += " AND "
            built_query += " nazwa = '{}' ".format(kennel_name)
            any_condition_present = True

        if region_id:
            if any_condition_present:
                built_query += " AND "
            built_query += " id_region = {} ".format(region_id)
            any_condition_present = True

        if built_query == "":
            cursor.execute(ALL_DOGS)
        else:
            cursor.execute(query + built_query)

        results = cursor.fetchall()
        return render_template('browser/kennels_list.html', kennels=results)