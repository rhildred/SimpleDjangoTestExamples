from django.test import TestCase

# Create your tests here.

from final.Q06 import translate_to_pig_latin

class Q8Tests(TestCase):
    def test_pig_latin(self):
        self.assertEqual(translate_to_pig_latin("scram"), "amscray")
        self.assertEqual(translate_to_pig_latin("I slept in"), 'Iay eptslay inay')
        self.assertEqual(translate_to_pig_latin("How long since the Train been gone?"), 'owHay onglay incesay ethay ainTray eenbay one?gay')
