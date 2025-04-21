# remainder division
# This program takes two integers as input and performs division, returning the quotient and remainder.

def main():
    divide_num = int(input("Please enter an integer to be divided :"))
    divide_by = int(input("Please enter an integer to be divide by :"))

    divide = divide_num / divide_by
    remainder = divide_num % divide_by

    print(f"The result of this division is {divide} with a remainder of {remainder}")


if __name__ == "__main__":
    main()