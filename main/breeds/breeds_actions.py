from flask import render_template, redirect, url_for, flash
from .sql import *
from ..utils import handle_postgres_error


def handle_add(request, cursor, conn):
    if request.method == 'POST':
        try:
            cursor.execute(GET_LATEST_ID)
            new_id = cursor.fetchall()[0][0] + 1
            breed_name_to_add = request.form.get('breed_name_to_add')
            breed_type_to_add = request.form.get('breed_type_to_add')
            is_working_dog_to_add = request.form.get('is_working_dog_to_add')
            is_working_dog_to_add = "true" if bool(is_working_dog_to_add) else "false"
            cursor.execute(ADD_BREED.format(new_id, breed_name_to_add, breed_type_to_add, is_working_dog_to_add))
            conn.commit()
            return redirect(url_for('browser.breeds'))
        except Exception as err:
            return handle_postgres_error(err, cursor, conn, 'editor.breeds')

def handle_delete(request, cursor, conn):
    if request.method == 'POST':
        try:
            breed_id_to_delete = request.form['breed_id_to_delete']
            cursor.execute(POSSIBLE_TO_DELETE_BREED.format(breed_id_to_delete))
            possible_to_delete_breed = cursor.fetchall()
            if possible_to_delete_breed[0][0]:
                cursor.execute(DELETE_BREED.format(breed_id_to_delete))
                conn.commit()
                return redirect(url_for('browser.breeds'))
            else:
                flash("Nie można usunąć rasy o id = {}, ponieważ referencję"
                    " do tego klucza znaleziono w innych tabelach".format(breed_id_to_delete))
                return redirect(url_for('editor.breeds'))
        except Exception as err:
            return handle_postgres_error(err, cursor, conn, 'editor.breeds')

def handle_edit(request, cursor, conn):
    if request.method == 'POST':
        try:
            breed_id_to_edit = request.form.get('breed_id_to_edit')
            breed_name_to_edit = request.form.get('breed_name_to_edit')
            breed_type_to_edit = request.form.get('breed_type_to_edit')
            is_working_dog_to_edit = request.form.get('is_working_dog_to_edit')
            is_working_dog_to_edit = "true" if bool(is_working_dog_to_edit) else "false"

            cursor.execute(UPDATE_BREED.format(breed_id_to_edit, breed_name_to_edit, breed_type_to_edit, is_working_dog_to_edit))
            conn.commit()
            return redirect(url_for('browser.breeds'))
        except Exception as err:
            return handle_postgres_error(err, cursor, conn, 'editor.breeds')

def handle_search(request, cursor):
    if request.method == 'GET':
        try:
            breed_name = request.args.get('breed_name')
            type = request.args.get('type')
            work_trail_yes = request.args.get('work_trail_yes')
            work_trail_no = request.args.get('work_trail_no')
            query = SEARCH_BREED
            any_condition_present = False
            built_query = ""
            if breed_name:
                built_query += " nazwa = '{}'".format(breed_name)
                any_condition_present = True

            if type:
                if any_condition_present:
                    built_query += " AND "
                built_query += " typ = '{}' ".format(type)
                any_condition_present = True

            if work_trail_yes == "Yes":
                if any_condition_present:
                    built_query += " AND "
                built_query += " proba_pracy = " + "true"

            elif work_trail_no == "No":
                if any_condition_present:
                    built_query += " AND "
                built_query += " proba_pracy = " + "false"


            if built_query == "":
                cursor.execute(ALL_BREEDS)
            else:
                cursor.execute(query + built_query)

            results = cursor.fetchall()
            return render_template('browser/breeds.html', breeds=results)
        except Exception as err:
            return handle_postgres_error(err, cursor, conn, 'browser.breeds')