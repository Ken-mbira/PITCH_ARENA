import unittest
from app.models import User

class UserModelTest(unittest.TestCase):

    def setUp(self):
        """This will run before every test does
        """
        self.new_user = User(password = 'banana')

    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)

    def test_no_access_password(self):
            with self.assertRaises(AttributeError):
                self.new_user.password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('banana'))

    def tearDown(self):
        User.query.delete()

    def test_instance(self):
        """This will check if the user instance is being created correctly
        """
        self.user = User(username = 'Ken Mbira',email = 'mbiraaa@gmail.com')

        self.assertEqual(self.user.username,'Ken Mbira')