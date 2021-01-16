from flask import render_template, redirect, url_for
from .sql import *

def handle_add(request, cursor, conn):
    if request.method == 'POST':
        cursor.execute(GET_LATEST_ID)
        new_id = cursor.fetchall()[0][0] + 1
        exam_name_to_add = request.form.get('exam_name_to_add')
        description_to_add = request.form.get('description_to_add')
        region_id_to_add = request.form.get('region_id_to_add')
        examiner_id_to_add = request.form.get('examiner_id_to_add')
        exam_date_to_add = request.form.get('exam_date_to_add')
        cursor.execute(ADD_EXAM.format(new_id, exam_name_to_add, description_to_add,
                                       region_id_to_add, examiner_id_to_add, exam_date_to_add))
        conn.commit()
        return redirect(url_for('browser.exams'))

def handle_delete(request, cursor, conn):
    if request.method == 'POST':
        exam_id_to_delete = request.form['exam_id_to_delete']
        cursor.execute(DELETE_EXAM.format(exam_id_to_delete))
        conn.commit()
        return redirect(url_for('browser.exams'))

def handle_edit(request, cursor, conn):
    if request.method == 'POST':
        exam_id_to_edit = request.form.get('exam_id_to_edit')
        exam_name_to_add = request.form.get('exam_name_to_add')
        description_to_add = request.form.get('description_to_add')
        region_id_to_add = request.form.get('region_id_to_add')
        examiner_id_to_add = request.form.get('examiner_id_to_add')
        exam_date_to_add = request.form.get('exam_date_to_add')
        cursor.execute(UPDATE_EXAM.format(exam_id_to_edit, exam_name_to_add, description_to_add,
                                       region_id_to_add, examiner_id_to_add), exam_date_to_add)
        conn.commit()
        return redirect(url_for('browser.exams'))

def handle_search(request, cursor):
    if request.method == 'GET':
        exam_id = request.args.get('exam_id')
        exam_name = request.args.get('exam_name')
        region_id = request.args.get('region_id')
        examiner_id = request.args.get('examiner_id')
        exam_date_start = request.args.get('exam_date_start')
        exam_date_end = request.args.get('exam_date_end')

        query = SEARCH_EXAMS
        built_query = ""
        any_condition_present = False
        if exam_id:
            built_query += " id = {}".format(exam_id)
            any_condition_present = True
        if exam_name:
            if any_condition_present:
                built_query += " AND "
            built_query += " nazwa = '{}'".format(exam_name)
            any_condition_present = True

        if region_id:
            if any_condition_present:
                built_query += " AND "
            built_query += " id_region = {}".format(region_id)
            any_condition_present = True

        if examiner_id:
            if any_condition_present:
                built_query += " AND "
            built_query += " id_egzaminator = {}".format(examiner_id)
            any_condition_present = True

        if exam_date_start and exam_date_end:
            if any_condition_present:
                built_query += " AND "
            built_query += " data_zaliczenia between '{}' AND '{}'".format(exam_date_start, exam_date_end)

        if built_query == "":
            cursor.execute(ALL_EXAMS)
        else:
            cursor.execute(query + built_query)

        results = cursor.fetchall()
        return render_template('browser/exams.html', exams=results)