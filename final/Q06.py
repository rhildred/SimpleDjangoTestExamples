def average_cals(aInput):
    nTotal = 0
    for nCals in aInput:
        nTotal += nCals
    return round(nTotal/len(aInput), 2)


if __name__ == "__main__":
    aDays = []
    nDays = 7

    try:
        for n in range(1, nDays + 1):
            aDays.append(int(input("Enter your calories for day " + str(n) +": ")))
        print("Your average calories for", nDays, "days was", average_cals(aDays))
    except:
        print("Please enter numeric values for all days.")
