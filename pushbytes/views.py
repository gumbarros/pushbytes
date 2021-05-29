"""
Views da aplicação
"""

from datetime import datetime
from flask import render_template
from pushbytes import app
from flask_login import login_required, current_user
from pushbytes.auth import login

@app.route('/')
def home():

    if current_user.is_authenticated:
        return render_template(
            'index.html',
            title='PushBytes',
            year=datetime.now().year,
            user=current_user
        )

    return login()
