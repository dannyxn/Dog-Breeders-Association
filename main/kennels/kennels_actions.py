from flask import render_template, redirect, url_for
from .sql import *


def handle_add(request, cursor, conn):
    if request.method == 'POST':
        kennel_name_to_add = request.form.get('kennel_name_to_add')
        breeder_id_to_add = request.form.get('breeder_id_to_add')
        region_id_to_add = request.form.get('region_id_to_add')
        cursor.execute(ADD_KENNEL.format(100, breeder_id_to_add, region_id_to_add, kennel_name_to_add))
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

