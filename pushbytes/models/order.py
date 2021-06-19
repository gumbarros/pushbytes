

"""
Classe que representa um pedido
"""

from sqlalchemy.orm import backref
from pushbytes import db

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id =  db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    games =  db.relationship('Game', secondary='order_games', lazy='subquery', backref=db.backref('orders', lazy=True))

    
order_games = db.Table('order_games', db.Column('order_id', db.Integer, db.ForeignKey('order.id')),db.Column('game_id', db.Integer, db.ForeignKey('game.id')))