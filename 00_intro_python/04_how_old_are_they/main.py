def main():
    # Define the ages of each friend based on the given riddle
    anton = 21  # Anton is 21 years old
    beth = anton + 6  # Beth is 6 years older than Anton
    chen = beth + 20  # Chen is 20 years older than Beth
    drew = chen + anton  # Drew's age is Chen's age + Anton's age
    ethan = chen  # Ethan is the same age as Chen

    # Print the results
    print(f"Anton is {anton}")
    print(f"Beth is {beth}")
    print(f"Chen is {chen}")
    print(f"Drew is {drew}")
    print(f"Ethan is {ethan}")

# This provided line is required at the end of the Python file to call the main() function.
if __name__ == '__main__':
    main()
