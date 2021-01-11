import os

from flask import Flask
from . import auth
from . import main
from . import browser
from . import editor



def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.register_blueprint(auth.bp)
    app.register_blueprint(main.bp)
    app.register_blueprint(browser.bp)
    app.register_blueprint(editor.bp)

    return app