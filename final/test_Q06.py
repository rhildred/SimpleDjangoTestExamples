from django.test import TestCase

# Create your tests here.
from final.Q06 import average_cals

class Q6Tests(TestCase):
    def test_cals(self):
        self.assertEqual(average_cals([200, 340, 500]), 346.67)
