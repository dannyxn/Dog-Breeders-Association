from flask import render_template, redirect, url_for, flash
from .sql import *
from ..utils import extract_if_any, handle_postgres_error

def handle_add(request, cursor, conn):
    if request.method == 'POST':
        try:
            cursor.execute(GET_LATEST_ID)
            new_id = cursor.fetchall()[0][0] + 1
            dog_name_to_add = request.form.get('dog_name_to_add')
            breeder_id_to_add = request.form.get('breeder_id_to_add')
            litter_id_to_add = request.form.get('litter_id_to_add')
            birth_date_to_add = request.form.get('birth_date_to_add')
            sex_to_add = request.form.get('sex_to_add')

            if litter_id_to_add == '':
                litter_id_to_add = 'null'
            breed_id_to_add = request.form.get('breed_id_to_add')
            cursor.execute(ADD_DOG.format(new_id, breeder_id_to_add, litter_id_to_add, breed_id_to_add, dog_name_to_add,
                                          birth_date_to_add, sex_to_add))
            conn.commit()
            return redirect(url_for('browser.dogs'))
        except Exception as err:
            return handle_postgres_error(err, cursor, conn, 'editor.dogs')

def handle_delete(request, cursor, conn):
    if request.method == 'POST':
        try:
            dog_id_to_delete = request.form['dog_id_to_delete']
            cursor.execute(POSSIBLE_TO_DELETE_DOG.format(dog_id_to_delete))
            possible_to_delete_dog = cursor.fetchall()
            if possible_to_delete_dog[0][0]:
                cursor.execute(DELETE_DOG.format(dog_id_to_delete))
                conn.commit()
            else:
                flash("Nie można usunąć psa o id = {}, ponieważ referencję"
                    " do tego klucza znaleziono w innych tabelach".format(dog_id_to_delete))
            return redirect(url_for('browser.dogs'))
        except Exception as err:
            return handle_postgres_error(err, cursor, conn, 'editor.dogs')

def handle_edit(request, cursor, conn):
    if request.method == 'POST':
        try:
            dog_id_to_edit = request.form.get('dog_id_to_edit')
            dog_name_to_edit = request.form.get('dog_name_to_edit')
            breeder_id_to_edit = request.form.get('breeder_id_to_edit')
            litter_id_to_edit = request.form.get('litter_id_to_edit')
            birth_date_to_edit = request.form.get('birth_date_to_edit')
            sex_to_edit = request.form.get('sex_to_edit')

            if litter_id_to_edit == '':
                litter_id_to_edit = 'null'
            breed_id_to_edit = request.form.get('breed_id_to_edit')
            cursor.execute(UPDATE_DOG.format(dog_id_to_edit, dog_name_to_edit, breeder_id_to_edit,
                                             litter_id_to_edit, breed_id_to_edit, birth_date_to_edit, sex_to_edit))
            conn.commit()
            return redirect(url_for('browser.dogs'))
        except Exception as err:
            return handle_postgres_error(err, cursor, conn, 'editor.dogs')

def handle_search(request, cursor, conn):
    if request.method == 'GET':
        try:
            dog_name = request.args.get('dog_name')
            breeder_id = request.args.get('breeder_id')
            litter_id = request.args.get('litter_id')
            breed_id = request.args.get('breed_id')
            query = SEARCH_DOGS
            any_condition_present = False
            built_query = ""
            if dog_name:
                built_query += " imie = '{}'".format(dog_name)
                any_condition_present = True

            if breeder_id:
                if any_condition_present:
                    built_query += " AND "
                built_query += " id_wlasciciel = {} ".format(breeder_id)
                any_condition_present = True

            if breed_id:
                if any_condition_present:
                    built_query += " AND "
                built_query += " id_rasa = {} ".format(breed_id)
                any_condition_present = True

            if litter_id:
                if any_condition_present:
                    built_query += " AND "
                built_query += " id_miot = {} ".format(litter_id)
                any_condition_present = True

            if built_query == "":
                cursor.execute(ALL_DOGS)
            else:
                cursor.execute(query + built_query)

            results = cursor.fetchall()
            return render_template('browser/dogs.html', dogs=results)

        except Exception as err:
            return handle_postgres_error(err, cursor, conn, 'browser.dogs')

def details(request, cursor, id, conn):
    if request.method == 'GET':
        try:
            cursor.execute(SEARCH_DOGS  + ' id = ' + str(id))
            dog_data = cursor.fetchall()[0]

            cursor.execute(DOGS_ALL_EXAMS.format(id))
            dogs_exams = cursor.fetchall()

            return render_template('browser/dog_details.html', dog_data=dog_data, dogs_exams=dogs_exams)
        except Exception as err:
            return handle_postgres_error(err, cursor, conn, 'browser.dogs')


def handle_add_passed_exam(request, cursor, conn, dog_id):
    if request.method == 'POST':
        try:
            exam_id = request.form.get('exam_id')
            cursor.execute(ADD_PASSED_EXAM.format(dog_id, exam_id))
            conn.commit()
            return redirect(url_for('browser.dog_details', id=dog_id))
        except Exception as err:
            return handle_postgres_error(err, cursor, conn, 'editor.dogs')