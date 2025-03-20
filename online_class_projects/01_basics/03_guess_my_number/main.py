import random

def main():
    # Generate the secret number
    secret_number = random.randint(1, 99)
    
    print("\n🎯 I am thinking of a number between 1 and 99... Try to guess it!\n")
    
    while True:
        try:
            # Get user input
            guess = int(input("Enter a guess: ").strip())

            # Check if the guess is within range
            if guess < 1 or guess > 99:
                print("⚠️ Please enter a number between 1 and 99!\n")
                continue  # Skip the rest of the loop and ask again

            # Compare guess with the secret number
            if guess < secret_number:
                print("📉 Your guess is too low.\n")
            elif guess > secret_number:
                print("📈 Your guess is too high.\n")
            else:
                print(f"🎉 Congrats! The number was: {secret_number} 🎉\n")
                break  # Exit loop when guessed correctly

        except ValueError:
            print("❌ Invalid input! Please enter a valid number.\n")

if __name__ == '__main__':
    main()
