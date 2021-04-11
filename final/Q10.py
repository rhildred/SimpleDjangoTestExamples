import random

class Block:
    def toss(self):
        aSides = ["D", "thank-you", "apple", "6", "car", "dog"]
        nSide = random.randint(0,5)
        return aSides[nSide]

if __name__ == "__main__":
    oBlock = Block()

    print(oBlock.toss())