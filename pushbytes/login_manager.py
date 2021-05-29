"""
Módulo do login_manager
"""


from flask_login.login_manager import LoginManager
from pushbytes.models.user import User
from pushbytes import app

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)
login_manager.login_message = 'Usuário não autorizado, por favor realize o login.'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
