import os
import psycopg2

from flask import Flask, g
from .auth import bp as auth_bp
from .main import bp as main_bp
from .browser import bp as browser_bp
from .editor import bp as editor_bp
from .database_config import *

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.config.update(
        SECRET_KEY = "SECRET_KEY"
    )
    with app.app_context():
        g.db_conn = psycopg2.connect(host=host, port=port, dbname=dbname, user=user, password=pw)

    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(browser_bp)
    app.register_blueprint(editor_bp)
    app.app_context().push()
    return app


