from flask import render_template, redirect, url_for, flash
from .sql import *
from ..utils import extract_if_any, handle_postgres_error
import sys


def handle_add(request, cursor, conn):
    if request.method == 'POST':
        try:
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
        except Exception as err:
            return handle_postgres_error(err, cursor, conn, 'editor.breeders')

def handle_delete(request, cursor, conn):
    if request.method == 'POST':
        try:
            breeder_id_to_delete = request.form['breeder_id_to_delete']
            cursor.execute(POSSIBLE_TO_DELETE_BREEDER.format(breeder_id_to_delete))
            possible_to_delete_breeder = cursor.fetchall()
            if possible_to_delete_breeder[0][0]:
                cursor.execute(DELETE_BREEDER.format(breeder_id_to_delete))
                conn.commit()
                return redirect(url_for('browser.breeders'))

            flash("Nie można usunąć hodowcy o id = {}, ponieważ referencję"
                        " do tego klucza znaleziono w innych tabelach".format(breeder_id_to_delete))
            return redirect(url_for('editor.breeders'))

        except Exception as err:
            return handle_postgres_error(err, cursor, conn, 'editor.breeders')


def handle_edit(request, cursor, conn):
    try:
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
    except Exception as err:
        return handle_postgres_error(err, cursor, conn, 'editor.breeders')


def handle_search(request, cursor, conn):
    if request.method == 'GET':
        try:
            breeder_id = request.args.get('breeder_id')
            breeder_name = request.args.get('breeder_name')
            breeder_surname = request.args.get('breeder_surname')
            query = SEARCH_BREEDER
            any_condition_present = False
            built_query = ""
            if breeder_id:
                built_query += " id = "  + breeder_id
                any_condition_present = True
            if breeder_name:
                if any_condition_present:
                    built_query += " AND "
                built_query += " imie = '{}' ".format(breeder_name)
                any_condition_present = True
            if breeder_surname:
                if any_condition_present:
                    built_query += " AND "
                built_query += " nazwisko = '{}' ".format(breeder_surname)

            if built_query == "":
                cursor.execute(ALL_BREEDERS)
            else:
                cursor.execute(query + built_query)

            results = cursor.fetchall()
            return render_template('browser/breeders.html', breeders=results)

        except Exception as err:
            return handle_postgres_error(err, cursor, conn, 'browser.breeders')


def details(cursor, id, conn):
    try:
        stats = []
        cursor.execute(SEARCH_BREEDER + ' id = ' + str(id))
        personal_data = cursor.fetchall()[0]

        cursor.execute(BREEDER_KENNELS_COUNT.format(id))
        stats.append(extract_if_any(cursor, True))

        cursor.execute(BREEDER_DOGS_COUNT.format(id))
        stats.append(extract_if_any(cursor, True))

        cursor.execute(BREEDER_BREEDS_COUNT.format(id))
        stats.append(extract_if_any(cursor, True))

        cursor.execute(BREEDER_REGIONS_COUNT.format(id))
        stats.append(extract_if_any(cursor, True))
        return render_template('browser/breeder_details.html', personal_data=personal_data, stats=stats)

    except Exception as err:
        return handle_postgres_error(err, cursor, conn, 'browser.breeders')


