def main():
    while True:
        # Prompt the user to enter their favorite animal
        animal = input("\nWhat's your favorite animal? ").strip()

        # Check if the input is empty
        if not animal:
            print("\nOops! You must enter an animal name. Try again.")
        # Check if input contains only alphabets and spaces (to allow multi-word animal names)
        elif not all(char.isalpha() or char.isspace() for char in animal):
            print("\nInvalid input! Please enter only letters (no numbers or symbols). Try again.")
        else:
            # Display the response with the user's input
            print(f"\nMy favorite animal is also {animal}!\n")
            break  # Exit the loop when valid input is received


# This provided line is required at the end of
# the Python file to call the main() function.
if __name__ == '__main__':
    main()
