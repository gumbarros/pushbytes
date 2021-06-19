from pushbytes.models.order import Order
from pushbytes.models.publisher import Publisher
from pushbytes.models.game import Game
from flask_admin import Admin,BaseView, expose
from flask_admin.contrib.sqla import ModelView
from pushbytes import app,db
from flask import redirect, url_for

class LogoutView(BaseView):
    @expose('/')
    def index(self):
        return redirect(url_for('auth.logout'))

admin = Admin(app, name='Pushbytes', template_mode='bootstrap4')
admin.add_view(ModelView(Publisher, db.session))
admin.add_view(ModelView(Game, db.session))
admin.add_view(ModelView(Order, db.session))
admin.add_view(LogoutView(name='Logout'))

