import random

def roll_dice():
    print("Rolling dice...")
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    print("Die 1:", d1)
    print("Die 2:", d2)
    print("Total value:", d1 + d2)

roll_dice()
