

# adj = input("Adjective: ")
# verb1 = input("Verb: ")
# verb2 = input("Verb: ")
# famous_person = input("Famous person: ")

# madlib = f"Computer programming is so {adj}! it makes me so excited all the time because \
# I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

# print(madlib)


print("\n🌿 Welcome to the Jungle Adventure! 🦁")
print("🌳 Fill in the blanks to create your own wild story!\n")

# User Inputs
name = input("Enter your name: ")
animal = input("Name a jungle animal: ")
sound = input("What sound does the animal make? ")
place = input("Name a jungle location (e.g., cave, river, treehouse): ")
food = input("Name a food you would bring: ")
object = input("Name an object you found in the jungle: ")

# Create the jungle adventure story using f-strings
story = f"""
One bright morning, {name} decided to explore the deep jungle. 🌿  
As they walked through the thick trees, they suddenly heard a loud *"{sound}!"* 🐾  

They turned around and saw a *{animal}* staring at them! 😲  
Instead of running away, {name} bravely took out their *{food}* and shared it with the {animal}.  
The {animal} happily ate it and became {name}'s new jungle friend! 🐒🍌  

Together, they explored a *{place}, where they found an ancient *{object}** covered in golden dust. ✨  
Was it a lost treasure? A magical artifact? {name} smiled, knowing this was just the beginning of an unforgettable adventure! 🌎💫  
"""

# Display the final story
print("\n" + "="*50)
print(story)
print("="*50 + "\n")