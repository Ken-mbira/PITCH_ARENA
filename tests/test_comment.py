import unittest

from app.models import Comment

class CommentModelTest(unittest.TestCase):
    """This will check if the behaviours of the comment class are all working

    Args:
        unittest ([type]): [description]
    """
    def setUp(self):
        """This runs before every test
        """
        self.new_comment = Comment(comment = "This is a very ineresting idea", upvote = 1)

    def test_instance(self):
        """This checks whether the instance is being instantiated correctly
        """
        self.assertIsInstance(self.new_comment,Comment)

    def test_match_instance(self):
        """This checks whether the values saved match the ones inputted
        """
        self.assertEqual(self.new_comment.comment,'This is a very ineresting idea','The comment does not match')
        self.assertEqual(self.new_comment.upvote,1)