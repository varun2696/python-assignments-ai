# ### Problem **7: Iterate both lists simultaneously**

# Given a two Python list. Write a program to iterate both lists simultaneously and display items from list1 in original order and items from list2 in reverse order.


def iterate_lists(list1, list2):
    for item1, item2 in zip(list1, reversed(list2)):
        print("List1:", item1, "\tList2 (reversed):", item2)

# Test the function
list1 = [1, 2, 3, 4, 5]
list2 = ['A', 'B', 'C', 'D', 'E']
iterate_lists(list1, list2)
