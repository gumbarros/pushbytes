"""
Classe que representa uma produtora
"""

from sqlalchemy.orm import backref
from pushbytes import db

class Publisher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150),nullable=False)
    games = db.relationship('Game', backref='publisher', lazy=True)

    def __str__(self):
        return self.name