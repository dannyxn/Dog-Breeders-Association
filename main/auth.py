import functools
import psycopg2
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from .utils import handle_postgres_error, extract_if_any

bp = Blueprint('auth', __name__, url_prefix='/auth')
host = "127.0.0.1"
port = "5432"
dbname = "postgres"
user = "postgres"
pw = "postgres"
conn = psycopg2.connect(host=host, port=port, dbname=dbname, user=user, password=pw)
cursor = conn.cursor()
cursor.execute("SET SEARCH_PATH TO zwiazek")


@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        try:
            name = request.form['name']
            surname = request.form['surname']
            password = request.form['password']
            email = request.form['email']
            phone_number = request.form['phone_number']
            cursor.execute("SELECT * FROM Pracownik_ostatni_indeks")
            new_id = cursor.fetchall()[0][0] + 1
            cursor.execute("INSERT INTO Pracownik(id, imie, nazwisko, email, haslo, numer_telefonu) values"
                           f"({new_id}, '{name}', '{surname}', '{email}', '{password}', '{phone_number}')")
            conn.commit()
            redirect(url_for('auth.login'))
        except Exception as err:
            return handle_postgres_error(err, cursor, conn, 'auth.register')


    return render_template('auth/register.html')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        try:
            session.pop('user_id', None)
            email = request.form.get('email')
            password = request.form.get('password')
            cursor.execute(f"SELECT id, imie, nazwisko FROM Pracownik WHERE email='{email}' AND haslo='{password}'")
            results = cursor.fetchall()
            if not results:
                flash('Błędne hasło lub adres e-mail.')
                return redirect(url_for('auth.login'))

            user_id = results[0][0]
            name = results[0][1]
            surname = results[0][2]

            session['user_id'] = user_id
            session['user'] = name + " " + surname
            flash('Zalogowano.')

            return redirect(url_for('main.index'))
        except Exception as err:
            handle_postgres_error(err, cursor, conn, 'auth.login')


    return render_template('auth/login.html')


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))
