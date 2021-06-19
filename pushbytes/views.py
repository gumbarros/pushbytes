"""
Views da aplicação
"""

from datetime import datetime
from pushbytes import app
from flask_login import login_required, current_user
from pushbytes.auth import login
from flask import redirect, url_for, render_template

@app.route('/')
def home():

    if current_user.is_authenticated:
        return redirect(url_for('admin.index'))

    return login()

