from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,RadioField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    """This class will define the form to create a pitch

    Args:
        FlaskForm ([type]): [description]
    """
    pitch_title = StringField('Enter the title of the pitch',validators=[Required()])
    pitch = StringField('Enter your pitch',validators=[Required()])
    pitch_category = RadioField('Enter the category of the pitch',validators=[Required()],choices=[('interview'),('promotion'),('Pickup lines'),('Comedy lines')])
    submit = SubmitField('Pitch')