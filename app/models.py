from werkzeug.security import generate_password_hash,check_password_hash

from . import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(100))
    pass_secure = db.Column(db.String(100))

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