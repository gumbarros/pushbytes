"""
Inicialização do app Flask
"""

import os
from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app = Flask(__name__)
app.secret_key='ifsp'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pushbytes.db'

from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)
app.register_blueprint(Blueprint('main', __name__))

db.init_app(app)

import pushbytes.login_manager
import pushbytes.views
