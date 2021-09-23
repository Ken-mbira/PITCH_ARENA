import unittest

from app.models import User,Pitch

class PitchModelTest(unittest.TestCase):
    """This will test all behaviours of the pitch model

    Args:
        unittest ([type]): [description]
    """
    def setUp(self):
        """This will run before every test does
        """
        self.pitch = Pitch(pitch_category = 'Promotion pitch',pitch="This beats the life")

    def test_instance(self):
        """This will check if the pitch instance is being instantiated correctly
        """
        self.assertIsInstance(self.pitch,Pitch)
        self.assertEqual(self.pitch.pitch_category,'Promotion pitch','The categories are not equal')
        self.assertEqual(self.pitch.pitch,'This beats the life',"The pitches don' seem to match")