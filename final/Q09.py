dictCountry = {"Argentina":"AR","Brazil":"BR","Canada":"CA", "Denmark":"DK", "Egypt":"EG", "France":"FR", "Germany":"DE", "Hungary":"HU", "India":"IN", "Japan":"JP"}

def getCountryCode(sCountry):
    global dictCountry
    return dictCountry[sCountry]

if __name__ == "__main__":
    try:
        sCountryName = input("Enter the name of a country: ")
        sCountryCode = getCountryCode(sCountryName)
        print("The code for", sCountryName, "is", sCountryCode)
    except:
        # there is a lot going on here!
        print("Please enter a country from", list(dictCountry.keys()))