import random

def print_usr():
    global name
    name = input("What is your name?\n>")
    print("Hello,", name)

print_usr()

def roll_dice():
    print("Rolling dice...")
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    print("Die 1:", d1)
    print("Die 2:", d2)
    sum = d1+d2
    print("Total value:", sum)
    if sum > 7:
        print(name," won!")
    else:
        print(name," lost")

roll_dice()
