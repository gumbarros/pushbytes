"""
Classe que representa uma produtora
"""

from pushbytes import db

class Publisher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150),nullable=False)