import math
#calculate volume

def getVolume(nRadius, nHeight):
    return round(math.pi * nRadius **2 * nHeight, 2)

if __name__ == "__main__":
    # input

    nRadius = int(input("radius (meters) >"))

    nHeight = int(input("height (meters) >"))

    #output
    print("the volume is", getVolume(nRadius, nHeight), "cubic meters")
    
