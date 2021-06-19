"""
Classe que representa um usuário
"""

from pushbytes import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150),nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(150))
    orders = db.relationship('Order', backref='user', lazy=True)

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def __str__(self):
        return self.name