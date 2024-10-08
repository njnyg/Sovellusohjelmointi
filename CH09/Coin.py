import random

class Coin():
    def __init__(self):
        self.sides = 1
    
    def toss_coin(self, tosses):
        attempts = 0
        while attempts < tosses:
            self.sides = random.randint(0,1)
            print(self.sides)
            attempts += 1
        print("\n")

coin1 = Coin()
coin1.toss_coin(10)
coin1.toss_coin(20)
coin1.toss_coin(50)

