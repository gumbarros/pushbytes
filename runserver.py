"""
This script runs the pushbytes application using a development server.
"""

from os import environ
from pushbytes import app
from pushbytes.db import db
from flask_admin import Admin
from pushbytes.models.user import User
from flask_admin.contrib.sqla import ModelView

if __name__ == '__main__':

    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555

    db.create_all()

    admin = Admin(app, name="PushBytes", template_mode="bootstrap4")

    admin.add_view(ModelView(User, db.session))

    app.run(HOST, PORT)