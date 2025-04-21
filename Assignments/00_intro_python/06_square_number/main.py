# def main():
#     print("\nWelcome to the Square Number Program!")
#     while True:
#         try:
#             num = float(input("\nType a number to see its square: "))
#             print(str(num) + " squared is " + str(num ** 2))
#             break  # Exit the loop if input is valid
#         except ValueError:
#             print("\n❌ Invalid input! Please enter a valid number.")


# # There is no need to edit code beyond this point
# if __name__ == '__main__':
#     main()

def main():
            print("\nWelcome to the Square Number Program!")

            while True:
                try:
                    num = float(input("\nType a number to see its square: "))

                    print(f"\n{num} squared is {num ** 2}\n")
                    break

                except ValueError:
                    print("\n❌ Invalid input! Please enter a valid number.")


if __name__ == '__main__':
    main()

