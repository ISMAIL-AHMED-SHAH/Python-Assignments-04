import random
from words import words
import string

print("\nWelcome to Hangman!")
print("-" * 20)

def get_valid_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)

    return word

def hangman():
    word = get_valid_word(words).upper()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        print("\nYou have", lives, "lives left and you have used these letters: ", " ".join(used_letters))

        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("\nCurrent word: ", " ".join(word_list))
        user_letters = input('Guess a letter: ').upper()
        if user_letters in alphabet - used_letters:
            used_letters.add(user_letters)
            if user_letters in word_letters:
                word_letters.remove(user_letters)
                print(f"\nCorrect! {user_letters} is in the word.")
            else:
                lives = lives - 1
                print(f"\nWrong! {user_letters} is not in the word.")
        elif user_letters in used_letters:
            print("\nInvalid character. Try again.")

    if lives == 0:
        print("\nYou died, Sorry. The word was", word)
    else:
        print("\nYou guessed the word", word, "correctly !!")

    print("\nThanks for playing!\n")

hangman()