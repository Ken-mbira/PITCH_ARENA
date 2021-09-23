from flask import render_template,redirect,url_for,flash
from flask_login import login_user
from flask_login.utils import login_required, logout_user

from ..models import User
from . import auth
from .forms import RegistrationForm,LoginForm
from .. import db
from ..email import mail_message

@auth.route('/login',methods = ["GET","POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(url_for('main.index'))
        flash('Invalid password or user name')
    return render_template('auth/login.html',login_form = login_form)

@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username = form.username.data, email = form.email.data ,password = form.password.data)
        db.session.add(user)
        db.session.commit()

        mail_message("Welcome to PITCH ARENA","email/welcome_user",user.email,user=user)

        return redirect(url_for('auth.login'))
    return render_template('auth/register.html',form = form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
