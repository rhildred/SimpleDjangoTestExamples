def average_marks(aInput):
    nTotal = 0
    for nCals in aInput:
        nTotal += nCals
    return round(nTotal/len(aInput), 2)


if __name__ == "__main__":
    aDays = []
    nLabs = 7

    try:
        for n in range(1, nLabs + 1):
            aDays.append(int(input("Enter your marks for lab " + str(n) +": ")))
        print("Your average mark for", nLabs, "labs was", average_marks(aDays))
    except:
        print("Please enter numeric values for all days.")
