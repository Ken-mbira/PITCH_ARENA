from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,RadioField,TextAreaField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    """This class will define the form to create a pitch

    Args:
        FlaskForm ([type]): [description]
    """
    pitch = StringField('Enter your pitch',validators=[Required()])
    pitch_category = RadioField('Enter the category of the pitch',validators=[Required()],choices=[('interview'),('promotion'),('Pickup lines'),('Comedy lines')])
    submit = SubmitField('Pitch')

class CommentForm(FlaskForm):
    """This will define all features of a comment form

    Args:
        FlaskForm ([type]): [description]
    """
    comment = TextAreaField('Comment here...',validators=[Required()])
    vote = RadioField('Upvote or downvote',validators=[Required()],choices=[(1),(-1)])
    submit = SubmitField('Comment')