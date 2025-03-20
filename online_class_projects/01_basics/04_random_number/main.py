import random

N_NUMBERS = 10  # Number of random numbers
MIN_VALUE = 1   # Minimum possible value
MAX_VALUE = 100 # Maximum possible value

def main():
    """ Generate and print 10 random numbers in the range 1 to 100 """
    print("\n🎲 Random Number Generator 🎲\n")
    for _ in range(N_NUMBERS):
        print(random.randint(MIN_VALUE, MAX_VALUE))

    print("\n🎲 Thank You! The End 🎲\n")

if __name__ == '__main__':
    main()
