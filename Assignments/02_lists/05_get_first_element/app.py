
# find out the first element of a list and print it
def get_first_element(lst):
    print("The first element is:", lst[0])


num_elements = int(input("Enter the number of elements in the list: "))
my_list = []  


for i in range(num_elements):
    element = input(f"Enter element {i + 1}: ")
    my_list.append(element)  


get_first_element(my_list)