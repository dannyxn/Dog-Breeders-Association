from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('main', __name__, url_prefix='/')

@bp.before_request
def before_request():
    if 'user_id' in session and 'user' in session:
        g.user = session['user']
        g.user_id = session['user_id']
    else:
        return redirect(url_for('auth.login'))

@bp.route('/')
def index():
    return render_template('index.html')
