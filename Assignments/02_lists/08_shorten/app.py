
# Shorten a list to a maximum length of 4 items.
# If the list is longer than 4 items, remove items from the end until it is 4 items long.


max_lenght = 4

def shorten(lst):
    while len(lst) > max_lenght:
        remove_item = lst.pop()
        print("Removed:",remove_item)

def main():
    lst = input("Enter a list of items separated by spaces: ").split()
    print("Original list:",lst)

    shorten(lst)
    print("Final List:",lst)

if __name__ == "__main__":
    main()