from flask import render_template,abort,flash,redirect
from flask.helpers import url_for
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
        return redirect(url_for('main.show_pitch'))

    return render_template('pitch/create_pitch.html',pitch = pitch_form)

@main.route('/pitch')
def show_pitch():
    """This function will display all the pitches
    """
    interview_pitches = Pitch.query.filter_by(pitch_category = 'interview').all()
    promotion_pitches = Pitch.query.filter_by(pitch_category = 'promotion').all()
    pickup_lines = Pitch.query.filter_by(pitch_category = 'Pickup lines').all()
    comedic_quips = Pitch.query.filter_by(pitch_category = 'Comedy lines').all()

    return render_template('pitch/pitch.html',interview_pitches = interview_pitches,promotion_pitches = promotion_pitches,pickup_lines = pickup_lines,comedic_quips = comedic_quips)