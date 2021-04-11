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
        return(nTotal)
    def clear(self):
        self.items = []

