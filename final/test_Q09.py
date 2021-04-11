from django.test import TestCase

# Create your tests here.

from final.Q09 import getCountryCode

class Q09Tests(TestCase):
    def test_Countries(self):
        sCountry = getCountryCode("Argentina")
        self.assertEqual(sCountry, 'AR')
        sCountry = getCountryCode("Brazil")
        self.assertEqual(sCountry, 'BR')
        sCountry = getCountryCode("Canada")
        self.assertEqual(sCountry, 'CA')
        sCountry = getCountryCode("Denmark")
        self.assertEqual(sCountry, 'DK')
