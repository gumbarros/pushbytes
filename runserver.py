"""
Execução do servidor
"""

from os import environ
from pushbytes import app
from pushbytes import db
from pushbytes.models.user import User

if __name__ == '__main__':

    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555

    app.run(HOST, PORT)