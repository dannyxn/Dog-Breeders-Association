from flask import render_template, redirect, url_for
from .sql import *

def handle_add(request, cursor, conn):
    if request.method == 'POST':
        cursor.execute(GET_LATEST_ID)
        new_id = cursor.fetchall()[0][0] + 1
        father_id_to_add = request.form.get('father_id_to_add')
        mother_id_to_add = request.form.get('mother_id_to_add')
        alias_to_add = request.form.get('alias_to_add')
        cursor.execute(ADD_LITTER.format(new_id, father_id_to_add, mother_id_to_add, alias_to_add))
        conn.commit()
        return redirect(url_for('browser.litters'))

def handle_delete(request, cursor, conn):
    if request.method == 'POST':
        litter_id_to_delete = request.form['litter_id_to_delete']
        cursor.execute(DELETE_LITTER.format(litter_id_to_delete))
        conn.commit()
        return redirect(url_for('browser.litters'))

def handle_edit(request, cursor, conn):
    if request.method == 'POST':
        litter_id_to_edit = request.form.get('litter_id_to_edit')
        father_id_to_edit = request.form.get('father_id_to_edit')
        mother_id_to_edit = request.form.get('mother_id_to_edit')
        alias_to_edit = request.form.get('alias_to_edit')
        cursor.execute(UPDATE_LITTER.format(litter_id_to_edit, father_id_to_edit, mother_id_to_edit,
                                            alias_to_edit))
        conn.commit()
        return redirect(url_for('browser.litters'))

def handle_search(request, cursor):
    if request.method == 'GET':
        litter_id = request.args.get('litter_id')
        father_id = request.args.get('father_id')
        mother_id = request.args.get('mother_id')
        query = SEARCH_LITTERS
        built_query = ""
        any_condition_present = False

        if litter_id:
            built_query += " id = {}".format(litter_id)
            any_condition_present = True
        if father_id:
            if any_condition_present:
                built_query += " AND "
            built_query += " id_ojciec = {}".format(father_id)
            any_condition_present = True

        if mother_id:
            if any_condition_present:
                built_query += " AND "
            built_query += " id_matka = {}".format(mother_id)
            any_condition_present = True

        if built_query == "":
            cursor.execute(ALL_LITTERS)
        else:
            cursor.execute(query + built_query)

        results = cursor.fetchall()
        return render_template('browser/litters.html', litters=results)