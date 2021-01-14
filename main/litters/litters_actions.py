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