import random

print("\nWelcome To Password Generator")
print("-" * 30)

# Corrected character set (no misplaced spaces, properly enclosed in quotes)
chars = '!\"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'

number = int(input("\nHow many passwords do you want? "))
length = int(input("\nHow long do you want your password to be? "))

print("\nGenerating Passwords...\n")

for pwd in range(number):
    password = ''.join(random.choice(chars) for _ in range(length))
    print(password)
