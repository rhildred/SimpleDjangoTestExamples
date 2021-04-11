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