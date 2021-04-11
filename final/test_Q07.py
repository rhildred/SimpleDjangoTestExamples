from django.test import TestCase

# Create your tests here.

from final.Q07 import num_Consonants, num_Vowels, num_Words

class Q7Tests(TestCase):
    def test_counts(self):
        sInput = "How long since the Train been gone?"

        self.assertEqual(num_Words(sInput), 7)
        self.assertEqual(num_Consonants(sInput), 17)
        self.assertEqual(num_Vowels(sInput), 11)
