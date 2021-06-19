"""
Rotas relacionados a autenticação de usuários
"""

from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from pushbytes.models.user import User
from pushbytes import db
from pushbytes.login_manager import login_manager
from datetime import datetime
from flask_login import login_required, login_user, logout_user, current_user
auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template(
        'index.html',
        title='Login',
        year=datetime.now().year,
        user=current_user
)

@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash('Por favor verifique seus dados e tente novamente.')
        return redirect(url_for('auth.login'))

    login_user(user, remember=remember)
    return redirect(url_for('admin.index'))



@auth.route('/signup')
def signup():
    return render_template(
        'signup.html',
        title='Registrar-se',
        year=datetime.now().year,
        user=current_user
)

@auth.route('/signup', methods=['POST'])
def signup_post():

    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    password_confirmation = request.form.get('password_confirmation')

    if not name or not email or not password:
        flash("Por favor preencha todos os campos.")
        return redirect(url_for('auth.signup'))

    if password != password_confirmation:
        flash("Confirmação de senha incorreta.")
        return redirect(url_for('auth.signup'))

    user = User.query.filter_by(email=email).first()

    if user: 
        flash("Email já cadastrado")
        return redirect(url_for('auth.signup'))

    new_user = User(name=name,email=email, password=generate_password_hash(password, method='sha256'))

    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
