from django.test import TestCase

# Create your tests here.

from final.Q02 import getVolume

class Q2Tests(TestCase):
    def test_volume(self):
        self.assertEqual(getVolume(10, 10), 3141.59, "calculate volume 10 cm radius 10 cm height")
        try:
            getVolume("asdf", 10)
            self.assertFalse(True, "shouldn't get here")
        except:
            self.assertFalse(False, "it should throw an exception and land here")
