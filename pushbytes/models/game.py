
"""
Classe que representa um jogo
"""

from pushbytes import db

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150),nullable=False)
    price = db.Column(db.Float, nullable=False)
    publisher_id = db.Column(db.Integer, db.ForeignKey('publisher.id'), nullable=False)
    year = db.Column(db.Integer, nullable=False)

    def __str__(self):
        return self.name