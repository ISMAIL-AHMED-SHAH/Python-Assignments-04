def main():
    # Function to get a valid float input from the user
    def get_valid_float(prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Invalid input! Please enter a valid number.")

    # Get the three side lengths of the triangle
    side1 = get_valid_float("What is the length of side 1? ")
    side2 = get_valid_float("What is the length of side 2? ")
    side3 = get_valid_float("What is the length of side 3? ")

    # Calculate perimeter
    perimeter = side1 + side2 + side3

    # Print the result
    print(f"The perimeter of the triangle is {perimeter}")

# This provided line is required at the end of the Python file to call the main() function.
if __name__ == '__main__':
    main()
