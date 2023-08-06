# ### Problem **4: Arrange string characters such that lowercase letters should come first**

# Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.


def sort_lowercase_first(input_string):
    lowercase_chars = ''.join([char for char in input_string if char.islower()])
    uppercase_chars = ''.join([char for char in input_string if char.isupper()])
    return lowercase_chars + uppercase_chars

# Test the function
input_string = "aBcDEfGhIjK"
result_string = sort_lowercase_first(input_string)
print("Original String:", input_string)
print("Sorted String:", result_string)
