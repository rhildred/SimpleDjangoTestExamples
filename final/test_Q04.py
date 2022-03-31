from django.test import TestCase

# Create your tests here.
from final.Q04 import average_marks

class Q6Tests(TestCase):
    def test_marks(self):
        self.assertEqual(average_marks([8, 7, 8]), 7.67)
