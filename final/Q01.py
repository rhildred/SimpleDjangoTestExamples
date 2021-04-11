
#calculate federal tax
def getFederalTax(nTaxable):
    if nTaxable <= 45282:
        nPrevious = 0
        nMarginal = .15
        nPreviousTax = 0
    elif nTaxable <= 90563:
        nPrevious = 45282
        nMarginal = .205
        nPreviousTax = 6792
    elif nTaxable <= 140388:
        nPrevious = 90563
        nMarginal = .26
        nPreviousTax = 16075
    elif nTaxable <= 200000:    
        nPrevious = 140388
        nMarginal = .29
        nPreviousTax = 29029
    else:
        nPrevious = 200000
        nMarginal = .33
        nPreviousTax = 46317
    return round((nTaxable - nPrevious) * nMarginal + nPreviousTax, 2)


if __name__ == "__main__":

    #prompt for taxable income
    nTaxable = int(input("Please enter your taxable income: "))
    #output
    print("tax on", nTaxable, "=", getFederalTax(nTaxable))
