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

def handle_search(request, cursor):
    if request.method == 'GET':
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

def extract_if_any(cursor, is_numeric):
    ret = cursor.fetchall()
    if ret:
        return ret[0][0]
    else:
        return 0

def details(cursor, id):
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