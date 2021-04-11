from django.test import TestCase

# Create your tests here.

from final.Q01 import getFederalTax

class Q2Tests(TestCase):
    def test_tax(self):
        self.assertEqual(getFederalTax(35000), 5250.0, "calculate federal tax on $35,000")
        self.assertEqual(getFederalTax(6000), 900.0, "calculate federal tax on $60,000")
        self.assertEqual(getFederalTax(100000), 18528.62, "calculate federal tax on $100,000")
        self.assertEqual(getFederalTax(150000), 31816.48, "calculate federal tax on $150,000")
        self.assertEqual(getFederalTax(220000), 52917.0, "calculate federal tax on $220,000")
        try:
            getFederalTax("asdf")
            self.assertFalse(True, "shouldn't get here")
        except:
            self.assertFalse(False, "it should throw an exception and land here")

