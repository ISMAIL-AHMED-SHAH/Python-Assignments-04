PROMPT: str = "\nWhat do you want? "
JOKE: str = "\nHere is a joke for you! Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'\n"
SORRY: str = "\nSorry, I only tell jokes. Try again.\nIn this program, you should only type 'Joke' to get a joke.\n"

def main():
    print("\nWelcome to the Joke Bot!")
    while True:
        user_input = input(PROMPT).strip()  # Get user input and remove extra spaces
        
        if not user_input:
            print("\nOops! You must enter a valid input. Try again.\nIn this program, you should only type 'Joke' to get a joke.\n")
            continue  # Ask for input again
        
        if user_input == "Joke":  # Check if input is exactly "Joke"
            print(JOKE)
            break  # Exit loop after telling the joke
        else:
            print(SORRY)
            break  # Exit loop after printing sorry message

if __name__ == "__main__":
    main()
