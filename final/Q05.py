class Item:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price
    def __str__(self):
        return(self.__name + "," + self.__price)
    def getName(self):
        return(self.__name)
    def getPrice(self):
        return(self.__price)

class CashRegister:
    def __init__(self):
        self.items = []
    def purchase_item(self, item):
        self.items.append(item)
    def show_items(self):
        sReturn = "Items in Cart" 
        for item in self.items:
            sReturn += "\n" + str(item)
        return sReturn
    def get_total(self):
        nTotal = 0
        for item in self.items:
            nTotal += float(item.getPrice())
        return round(nTotal, 2)
    def clear(self):
        self.items = []

if __name__ == "__main__":

    items = [Item("Jacket", "59.95"),
            Item("Designer Jeans", "34.95"),
            Item("Shirt", "24.95")]
    cash = CashRegister()
    nItem = 1

    while nItem > 0:
        print("Please Enter an item to purchase. Enter 0 to checkout, C to clear")
        nItem = 0
        for item in items:
            nItem += 1
            print(nItem, item)
        sItem = input("please enter an item no >")
        if sItem.upper()  == "C":
            cash.clear()
            print(cash.show_items())
        else:
            try:
                nItem = int(sItem)
                if nItem > 0:
                    cash.purchase_item(items[nItem - 1])
                    print(cash.show_items())
            except:
                print("Please enter an item number, C or 0")

    print(cash.show_items())
    print("total:", cash.get_total())
