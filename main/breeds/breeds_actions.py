from flask import render_template, redirect, url_for
from .sql import *

def handle_add(request, cursor, conn):
    if request.method == 'POST':
        breed_name_to_add = request.form.get('breed_name_to_add')
        breed_type_to_add = request.form.get('breed_type_to_add')
        is_working_dog_to_add = request.form.get('is_working_dog_to_add')
        is_working_dog_to_add = "true" if bool(is_working_dog_to_add) else "false"
        cursor.execute(ADD_BREED.format(100, breed_name_to_add, breed_type_to_add, is_working_dog_to_add))
        conn.commit()
        return redirect(url_for('browser.breeds'))

def handle_delete(request, cursor, conn):
    if request.method == 'POST':
        breed_id_to_delete = request.form['breed_id_to_delete']
        cursor.execute(DELETE_BREED.format(breed_id_to_delete))
        conn.commit()
        return redirect(url_for('browser.breeds'))

def handle_edit(request, cursor, conn):
    if request.method == 'POST':
        breed_id_to_edit = request.form.get('breed_id_to_edit')
        breed_name_to_edit = request.form.get('breed_name_to_edit')
        breed_type_to_edit = request.form.get('breed_type_to_edit')
        is_working_dog_to_edit = request.form.get('is_working_dog_to_edit')
        is_working_dog_to_edit = "true" if bool(is_working_dog_to_edit) else "false"
        cursor.execute(UPDATE_BREED.format(breed_id_to_edit, breed_name_to_edit, breed_type_to_edit, is_working_dog_to_edit))
        conn.commit()
        return redirect(url_for('browser.breeds'))