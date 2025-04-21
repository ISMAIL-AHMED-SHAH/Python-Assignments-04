

# Simulate rolling two dice, and prints results of each roll as well as the total.

import random

max_num = 6

def main():
    dice1 = random.randint(1,max_num)
    dice2 = random.randint(1,max_num)
    total = dice1 + dice2

    print(f"Dice-1: {dice1} , Dice-2: {dice2}")
    print(f"Total : {total}")

if __name__ == "__main__":
    main()
