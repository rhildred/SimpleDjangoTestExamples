def average_cals(aInput):
    nTotal = 0
    for nCals in aInput:
        nTotal += nCals
    return round(nTotal/len(aInput), 2)
