from werkzeug.exceptions import HTTPVersionNotSupported
from pushbytes.models.order import Order
from pushbytes.models.publisher import Publisher
from pushbytes.models.game import Game
from flask_admin import Admin,BaseView, expose
from flask_admin.contrib.sqla import ModelView
from flask_admin.base import AdminIndexView
from pushbytes import app,db
from flask import redirect, url_for

class PushbytesIndex(AdminIndexView):
    @expose('/')
    def index(self):

        total_games = Game.query.count()
        total_orders = Order.query.count()
        total_publishers = Publisher.query.count()

        return self.render('admin/index.html', total_games=total_games,  total_orders=total_orders,total_publishers=total_publishers)

class LogoutView(BaseView):
    @expose('/')
    def index(self):
        return redirect(url_for('auth.logout'))

admin = Admin(app, name='Pushbytes', template_mode='bootstrap4',index_view=PushbytesIndex())
admin.add_view(ModelView(Publisher, db.session))
admin.add_view(ModelView(Game, db.session))
admin.add_view(ModelView(Order, db.session))
admin.add_view(LogoutView(name='Logout'))

