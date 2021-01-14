from flask import render_template, redirect, url_for
from .sql import *

def handle_add(request, cursor, conn):
    if request.method == 'POST':
        exam_name_to_add = request.form.get('exam_name_to_add')
        description_to_add = request.form.get('description_to_add')
        region_id_to_add = request.form.get('region_id_to_add')
        examiner_id_to_add = request.form.get('examiner_id_to_add')
        exam_date_to_add = request.form.get('exam_date_to_add')
        cursor.execute(ADD_EXAM.format(100, exam_name_to_add, description_to_add,
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