
# Fill out the last element in the list. 


def get_first_element(lst):
    print("The last element is:", lst[-1])


num_elements = int(input("Enter the number of elements in the list: "))
my_list = []  


for i in range(num_elements):
    element = input(f"Enter element {i + 1}: ")
    my_list.append(element)  


get_first_element(my_list)
