from flask import render_template,abort,flash
from flask_login import login_required,current_user

from app.models import Pitch, User, db
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

@main.route('/create',methods = ["GET","POST"])
@login_required
def create_pitch():
    """This will create the pitch according to the category
    """
    pitch_form = PitchForm()
    if pitch_form.validate_on_submit():
        pitch = Pitch(pitch = pitch_form.pitch.data,pitch_category = pitch_form.pitch_category.data,user_id = current_user.id)
        db.session.add(pitch)
        db.session.commit()
        flash ("Pitch created")

    return render_template('pitch.html',pitch = pitch_form)