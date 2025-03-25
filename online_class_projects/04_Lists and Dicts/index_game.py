def access_element(lst, index):
    """Returns the element at the specified index with error handling."""
    try:
        return f"Element at index {index}: {lst[index]}"
    except IndexError:
        return "Error: Index out of range!"

def modify_element(lst, index, new_value):
    """Modifies the element at the given index with error handling."""
    try:
        lst[index] = new_value
        return f"Updated list: {lst}"
    except IndexError:
        return "Error: Index out of range!"

def slice_list(lst, start, end):
    """Returns a sliced list with error handling."""
    if start < 0 or end > len(lst) or start > end:
        return "Error: Invalid slice range!"
    return f"Sliced list: {lst[start:end]}"

def sort_list(lst, order="asc"):
    """Sorts the list in ascending or descending order."""
    if order == "asc":
        lst.sort()
        return f"List sorted in ascending order: {lst}"
    elif order == "desc":
        lst.sort(reverse=True)
        return f"List sorted in descending order: {lst}"
    else:
        return "Error: Invalid order! Use 'asc' or 'desc'."

def remove_element(lst, value):
    """Removes the element if it exists in the list."""
    if value in lst:
        lst.remove(value)
        return f"'{value}' removed. Updated list: {lst}"
    else:
        return f"Error: '{value}' not found in the list."

def search_element(lst, value):
    """Checks if an element exists in the list."""
    return f"'{value}' found in the list!" if value in lst else f"'{value}' not found in the list."

def main():
    my_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    
    while True:
        print("\nChoose an operation:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Sort the list")
        print("5. Remove an element")
        print("6. Search for an element")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ").strip()

        if choice == '1':  # Access an element
            index = int(input("Enter an index: "))
            print(access_element(my_list, index))

        elif choice == '2':  # Modify an element
            index = int(input("Enter an index: "))
            new_value = input("Enter the new value: ")
            print(modify_element(my_list, index, new_value))

        elif choice == '3':  # Slice the list
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            print(slice_list(my_list, start, end))

        elif choice == '4':  # Sort the list
            order = input("Enter sorting order (asc/desc): ").strip().lower()
            print(sort_list(my_list, order))

        elif choice == '5':  # Remove an element
            value = input("Enter the value to remove: ").strip()
            print(remove_element(my_list, value))

        elif choice == '6':  # Search for an element
            value = input("Enter the value to search: ").strip()
            print(search_element(my_list, value))

        elif choice == '7':  # Exit
            print("Exiting the game. Goodbye!")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 7.")

# Run the game
main()
