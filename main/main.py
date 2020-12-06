from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/')
def index():
    return render_template('main/index.html')