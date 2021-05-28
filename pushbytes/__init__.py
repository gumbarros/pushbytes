"""
The flask application package.
"""

import os
from flask import Flask

app = Flask(__name__)
app.secret_key='ifsp'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

import pushbytes.views
