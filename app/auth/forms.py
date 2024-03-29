from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,ValidationError
from wtforms.fields.core import BooleanField
from wtforms.validators import Required,Email,EqualTo

from ..models import User

class RegistrationForm(FlaskForm):
    """This is the class that defines the registration of a new user

    Args:
        FlaskForm ([moduel]): [Where the form characteristics are inherited from]

    Raises:
        ValidationError: [This will be raised when a user uses an email that is alredy present in the database]
        ValidationError: [This will be raised when a user uses an password that is alredy present in the database]
    """
    email = StringField('Your Email Address',validators=[Required(),Email()])
    username = StringField('Enter your username',validators = [Required()])
    password = PasswordField('Password',validators = [Required(), EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords',validators = [Required()])
    submit = SubmitField('Sign Up')

    def validate_email(self,data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError('There is an account with that email')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')

class LoginForm(FlaskForm):
    """This is the class that defines the form used for the loging in

    Args:
        FlaskForm ([module]): [This is where we inherit the form functionality]
    """
    email = StringField('Enter the email',validators=[Required(),Email()])
    password = PasswordField('Enter your password',validators=[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')
