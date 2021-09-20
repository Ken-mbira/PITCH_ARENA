from datetime import datetime
from flask_login import UserMixin

from werkzeug.security import generate_password_hash,check_password_hash

from . import db,login_manager

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin,db.Model):
    """This will define all behaviours within the user class

    Args:
        UserMixin ([type]): [description]
        db ([model]): [This is to connect the user to the database]

    Raises:
        AttributeError: [This will be the case when one tries to access the password]

    Returns:
        [dict]: [This is what will be returned when one views the user class and its contents]
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique=True,index=True)
    pass_secure = db.Column(db.String(255))
    pitches = db.relationship('Pitch',backref = 'pitche',lazy = "dynamic")
    profile_pic_path = db.Column(db.String(255))

    @property
    def password(self):
        """This will prevent reading of the password
        """
        raise AttributeError('You cannot read the password')

    @password.setter
    def password(self,password):
        """This will turn the password into hashes

        Args:
            password ([string]): [This is the input password]
        """
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        """This will check the set series of hashes and the hashes from the inputted password to see if they match

        Args:
            password ([string]): [This is the input password]
        """
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'


class Pitch(db.Model):
    """This will define all behaviours of the comments

    Args:
        UserMixin ([type]): [description]
        db ([Model]): [This will connect all the comments to the database]
    """
    __tablename__ = 'pitches'

    pitch_id = db.Column(db.Integer,primary_key=True)
    pitch_category = db.Column(db.String(255))
    pitch = db.Column(db.String(255))
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    comments = db.relationship('Comment',backref = 'commente',lazy = "dynamic")

    def __repr__(self):
        return f'Pitch {self.pitch}'

class Comment(db.Model):
    """This is the comment class and it will define all the behaviours of the comments

    Args:
        db ([Model]): [This will connect all the comments to the database]
    """

    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key=True)
    comment = db.Column(db.String(255))
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.pitch_id'))

    def __repr__(self):
        return f'Comment {self.comment}'
