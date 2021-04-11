# Q03 is a subset of Q07

sVowels = "aeiou"

def num_Vowels(sInput):
    nVowels = 0
    for ch in sInput:
        if ch in sVowels:
            nVowels += 1
    return nVowels

def num_Consonants(sInput):
    nConsonants = 0
    for ch in sInput:
        if ch not in sVowels and ch not in " .,!>?":
            nConsonants += 1
    return nConsonants

if __name__ == "__main__":
    sUserInput = input("enter a string >")

    print("the string contains", num_Vowels(sUserInput), "Vowels")

    print("the string contains", num_Consonants(sUserInput), "Consonants")
