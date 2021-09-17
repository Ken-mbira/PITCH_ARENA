from flask_login import UserMixin

from werkzeug.security import generate_password_hash,check_password_hash

from . import db,login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

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
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index=True)
    pass_secure = db.Column(db.String(255))

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