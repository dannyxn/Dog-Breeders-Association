import psycopg2
from flask import g
from .database_config import *

def get_db():
    if 'db' not in g:
        g.conn = psycopg2.connect(host=host, port=port, dbname=dbname, user=user, password=pw)
        g.cursor = g.conn.cursor()
        g.cursor.execute("SET SEARCH_PATH TO public")

    return g.conn, g.cursor