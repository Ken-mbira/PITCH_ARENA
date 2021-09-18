from flask import render_template,abort
from flask_login import login_required,current_user

from app.models import User
from . import main

@main.route('/')
def index():
    title = 'PITCH ARENA'
    return render_template('index.html',title = title)

@main.route('/profile/<username>')
@login_required
def profile(username):
    user = User.query.filter_by(username = username).first()
    if user is None:
        abort(404)
    
    return render_template('profile/profile.html',user = user)