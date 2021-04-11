from django.test import TestCase

# Create your tests here.

from final.Q04 import addPrice, deletePrice, listPrices 

class Q4Tests(TestCase):
    def test_prices(self):
        addPrice("tomatoes", 2.99)
        self.assertEqual(listPrices(), 'Name is: tomatoes Price is: 2.99\n', "should be tomatoes")
        deletePrice("tomatoes")
        self.assertEqual(listPrices(), "", "should be empty")
