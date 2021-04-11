from django.test import TestCase

# Create your tests here.

from final.Q09 import getCountryCode

class Q09Tests(TestCase):
    def test_Argentina(self):
        sCountry = getCountryCode("Argentina")
        self.assertEqual(sCountry, 'AR')
    def test_Brazil(self):
        sCountry = getCountryCode("Brazil")
        self.assertEqual(sCountry, 'BR')
    def test_Canada(self):
        sCountry = getCountryCode("Canada")
        self.assertEqual(sCountry, 'CA')
    def test_Denmark(self):
        sCountry = getCountryCode("Denmark")
        self.assertEqual(sCountry, 'DK')
