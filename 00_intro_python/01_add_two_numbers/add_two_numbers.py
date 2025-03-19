# """
# Program: add2numbers
# --------------------
# Another python program to get some practice with
# variables.  This program asks the user for two
# integers and prints their sum.
# """


# def main():
#     print("This program adds two numbers.")
#     num1 : str = input("Enter first number: ")
#     num1 : int = int(num1)
#     num2  : str = input("Enter second number: ")
#     num2 : int = int(num2)
#     total : int = num1 + num2
#     print("The total is " + str(total) + ".")


# # This provided line is required at the end of
# # Python file to call the main() function.
# if __name__ == '__main__':
#     main()




def main():
    print("\nThis program adds two numbers.")

    while True:
        try:
            num1 = int(input("\nEnter the first number: "))

            if num1 == 0:
                break


            num2 = int(input("\nEnter the second number: "))

            total = num1 + num2
            print(f"\nThe total is {total}.")

            print("\nEnter 0 to exit the program.\n")
        except ValueError:
            print("❌ Invalid input! Please enter integer values only.")


if __name__ == '__main__':
    main()