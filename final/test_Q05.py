from django.test import TestCase

# Create your tests here.

from final.Q05 import CashRegister, Item

class Q5Tests(TestCase):
    def test_cash(self):

        cash = CashRegister()

        cash.purchase_item(Item("Designer Jeans", "34.95"))

        self.assertEqual(cash.show_items(), "Items in Cart\nDesigner Jeans,34.95" )

        self.assertEqual(cash.get_total(), 34.95, "total in cart")
