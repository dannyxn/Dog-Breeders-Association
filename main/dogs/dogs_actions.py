from flask import render_template, redirect, url_for
from .sql import *

def handle_add(request, cursor, conn):
    if request.method == 'POST':
        cursor.execute(GET_LATEST_ID)
        new_id = cursor.fetchall()[0][0] + 1
        dog_name_to_add = request.form.get('dog_name_to_add')
        breeder_id_to_add = request.form.get('breeder_id_to_add')
        litter_id_to_add = request.form.get('litter_id_to_add')
        if litter_id_to_add == '':
            litter_id_to_add = 'null'
        breed_id_to_add = request.form.get('breed_id_to_add')
        cursor.execute(ADD_DOG.format(new_id, breeder_id_to_add, litter_id_to_add, breed_id_to_add, dog_name_to_add))
        conn.commit()
        return redirect(url_for('browser.dogs'))

def handle_delete(request, cursor, conn):
    if request.method == 'POST':
        dog_id_to_delete = request.form['dog_id_to_delete']
        cursor.execute(DELETE_DOG.format(dog_id_to_delete))
        conn.commit()
        return redirect(url_for('browser.dogs'))

def handle_edit(request, cursor, conn):
    if request.method == 'POST':
        dog_id_to_edit = request.form.get('dog_id_to_edit')
        dog_name_to_edit = request.form.get('dog_name_to_edit')
        breeder_id_to_edit = request.form.get('breeder_id_to_edit')
        litter_id_to_edit = request.form.get('litter_id_to_edit')
        if litter_id_to_edit == '':
            litter_id_to_edit = 'null'
        breed_id_to_edit = request.form.get('breed_id_to_edit')
        cursor.execute(UPDATE_DOG.format(dog_id_to_edit, dog_name_to_edit, breeder_id_to_edit,
                                         litter_id_to_edit, breed_id_to_edit))
        conn.commit()
        return redirect(url_for('browser.dogs'))