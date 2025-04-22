
# find a list by taking input from the user until the user enters an empty string.
# Enter a value: 1 Enter a value: 2 Enter a value: 3 Enter a value: Here's the list: ['1', '2', '3']


def main():
    my_list = []

    while True:
        value = input("Enter a value :")
        if value == "":
            break
        my_list.append(value)
    
    print(f"Here's the List: {my_list}")

if __name__ == "__main__":
    main()