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
