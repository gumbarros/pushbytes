from pushbytes.models.publisher import Publisher
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from pushbytes import app,db

admin = Admin(app, name='Pushbytes', template_mode='bootstrap4')
admin.add_view(ModelView(Publisher, db.session))