import random

NUM_ROUNDS = 5  # Total rounds to play

def main():
    print("Welcome to the High-Low Game!")
    print("-" * 32)

    score = 0  # Track the user's score

    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"Round {round_num}")
        user_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)

        print(f"Your number is {user_number}")
        guess = input("Do you think your number is higher or lower than the computer's? (higher/lower): ").strip().lower()

        # Ensure valid input
        while guess not in ["higher", "lower"]:
            guess = input("Please enter either 'higher' or 'lower': ").strip().lower()

        # Determine if the guess is correct
        if (guess == "higher" and user_number > computer_number) or (guess == "lower" and user_number < computer_number):
            print("You were right!", end=" ")
            score += 1  # Increase score
        else:
            print("Aww, that's incorrect.", end=" ")

        print(f"The computer's number was {computer_number}")
        print(f"Your score is now {score}\n")

    # Final message based on score
    print("Thanks for playing!")
    if score == NUM_ROUNDS:
        print("Wow! You played perfectly! 🎯")
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well! 👍")
    else:
        print("Better luck next time! 😅")

if __name__ == '__main__':
    main()
