
def main():
    # create a list
    fruits = ["apple", "banana", "cherry", "orange", "grape"]
    print(f"\nFruit List : ", fruits)

    # print the list
    print(f"\nLength of the list: {len(fruits)}")
    
    # add mango to the list
    fruits.append("mango")

    # updated list
    print(f"\nUpdated fruit List : {fruits}\n")

    # updated length of the list
    print(f"\nLength of the list: {len(fruits)}")

    # remove the last item from the list
    fruits.pop()
    print(f"\nUpdated fruit List : {fruits}\n")

    # remove the first item from the list
    fruits.pop(0)
    print(f"\nUpdated fruit List : {fruits}\n")

    # remove the item "cherry" from the list
    fruits.remove("cherry")
    print(f"\nUpdated fruit List : {fruits}\n")

    # insert "cherry" back to the list
    fruits.insert(1, "cherry")
    print(f"\nUpdated fruit List : {fruits}\n")

    # sort the list
    fruits.sort()
    print(f"\nSorted fruit List : {fruits}\n")

    # reverse the list
    fruits.reverse()
    print(f"\nReversed fruit List : {fruits}\n")

    # clear the list
    fruits.clear()
    print(f"\nCleared fruit List : {fruits}\n")

if __name__ == '__main__':
    main()

