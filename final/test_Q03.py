from django.test import TestCase

# Create your tests here.

from final.Q03 import num_Consonants, num_Vowels

class Q3Tests(TestCase):
    def test_counts(self):
        sInput = "I am just a poor boy. From a poor family."

        self.assertEqual(num_Consonants(sInput), 18)
        self.assertEqual(num_Vowels(sInput), 12)
