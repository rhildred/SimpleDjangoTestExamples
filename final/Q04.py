dictPrices = {}

def addPrice(sName, sPrice):
    global dictPrices
    dictPrices[sName] = sPrice

def deletePrice(sName):
    global dictPrices
    del dictPrices[sName]

def listPrices():
    global dictPrices
    sReturn = ""
    for sName in dictPrices:
        sReturn += "Name is: " + sName + " Price is: " + str(dictPrices[sName]) + "\n"
    return sReturn

if __name__ == "__main__":

    while True:

        print("Choices:")
        print(" 1 to add")
        print(" 2 to delete")
        print(" 3 to list")
        print(" 4 to quit")

        sChoice = input("What is your choice? ")
        if(sChoice == "1"):
            sName = input("name ")
            sPrice = input("price ")
            addPrice(sName, sPrice)
            print(listPrices())
        elif(sChoice == "2"):
            sName = input("name ")
            deletePrice(sName)
            print(listPrices())
        elif(sChoice == "3"):
            print(listPrices())
        else:
            break
