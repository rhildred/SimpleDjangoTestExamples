from django.test import TestCase

# Create your tests here.

from final.Q10 import Block

class Q10Test(TestCase):
    def test_toss(self):
        oBlock = Block()
        sSide = oBlock.toss()
        self.assertTrue(sSide == "D" or sSide == "apple" or 
        sSide == "thank-you" or sSide == "6" or sSide == "car" or sSide == "dog")
