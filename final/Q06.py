def translate_to_pig_latin(sInput):
    aInput = sInput.split(" ")

    sOutput = ""

    for sWord in aInput:
        nFirst = 0
        for ch in sWord:
            if ch in "aeiou":
                break
            else:
                nFirst += 1
        if sOutput != "":
            sOutput += " "
        sOutput += sWord[nFirst:len(sWord)] + sWord[:nFirst] + "ay"
    return sOutput

if __name__ == "__main__":
    sInput = input("Enter an English phrase to translate: ")
    sOutput = translate_to_pig_latin(sInput)
    print(sOutput)