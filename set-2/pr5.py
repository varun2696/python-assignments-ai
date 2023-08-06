# ### Problem **5: Concatenate two lists index-wise**

# Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.



def add_lists_indexwise(list1, list2):
    new_list = []
    min_length = min(len(list1), len(list2))

    for i in range(min_length):
        new_list.append(list1[i] + list2[i])

    if len(list1) > min_length:
        new_list.extend(list1[min_length:])
    elif len(list2) > min_length:
        new_list.extend(list2[min_length:])

    return new_list

# Test the function
list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40]
result_list = add_lists_indexwise(list1, list2)
print("List 1:", list1)
print("List 2:", list2)
print("Result List:", result_list)
