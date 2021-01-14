from flask import render_template, redirect, url_for
from .sql import *

def handle_add(request, cursor, conn):
    if request.method == 'POST':
        cursor.execute(GET_LATEST_ID)
        new_id = cursor.fetchall()[0][0] + 1
        breeder_name_to_add = request.form.get('breeder_name_to_add')
        breeder_surname_to_add = request.form.get('breeder_surname_to_add')
        breeder_email_to_add = request.form.get('breeder_email_to_add')
        breeder_phone_number_to_add = request.form.get('breeder_phone_number_to_add')
        cursor.execute(ADD_BREEDER.format(new_id, breeder_name_to_add, breeder_surname_to_add, breeder_email_to_add,
                                         breeder_phone_number_to_add))
        conn.commit()
        return redirect(url_for('browser.breeders'))

def handle_delete(request, cursor, conn):
    if request.method == 'POST':
        breeder_id_to_delete = request.form['breeder_id_to_delete']
        cursor.execute(DELETE_BREEDER.format(breeder_id_to_delete))
        conn.commit()
        return redirect(url_for('browser.breeders'))

def handle_edit(request, cursor, conn):
    if request.method == 'POST':
        breeder_id_to_edit = request.form.get('breeder_id_to_edit')
        breeder_name_to_edit = request.form.get('breeder_name_to_edit')
        breeder_surname_to_edit = request.form.get('breeder_surname_to_edit')
        breeder_email_to_edit = request.form.get('breeder_email_to_edit')
        breeder_phone_number_to_edit = request.form.get('breeder_phone_number_to_edit')
        cursor.execute(UPDATE_BREEDER.format(breeder_id_to_edit, breeder_name_to_edit, breeder_surname_to_edit,
                                            breeder_email_to_edit, breeder_phone_number_to_edit))
        conn.commit()
        return redirect(url_for('browser.breeders'))