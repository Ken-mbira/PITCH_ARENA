from flask import render_template,abort
from flask_login import login_required,current_user

from app.models import User
from . import main
from .forms import PitchForm

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

@main.route('/create')
@login_required
def create_pitch():
    """This will create the pitch according to the category
    """
    pitch = PitchForm()
    return render_template('pitch.html',pitch = pitch)