from flask import render_template,redirect,url_for

from ..models import User
from . import auth
from .forms import RegistrationForm,LoginForm
from .. import db

@auth.route('/login')
def login():
    login_form = LoginForm()
    return render_template('auth/login.html',login_form = login_form)

@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username = form.username.data, email = form.email.data ,password = form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html',registration_form = form)