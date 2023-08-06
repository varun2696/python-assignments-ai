# Problem 10: Modify the tuple
# Given a nested tuple. Write a program to modify the first item (22) of a list inside the following tuple to 222
# Given:
# tuple1 = (11, [22, 33], 44, 55)


# <====>
# In Python, tuples are immutable, meaning their elements cannot be changed once they are created. However, if a tuple contains mutable objects (e.g., lists), you can modify the elements inside those mutable objects. 


tuple1 = (11, [22, 33], 44, 55)

# Convert the tuple to a list to modify the nested list
nested_list = list(tuple1)

# Modify the first item (22) of the list inside the tuple
nested_list[1][0] = 222

# Convert the list back to a tuple
modified_tuple = tuple(nested_list)

print("Original Tuple:", tuple1)
print("Modified Tuple:", modified_tuple)
