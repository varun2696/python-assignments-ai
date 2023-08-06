# ### Problem **3: Append new string in the middle of a given string**

# Given two strings, `s1` and `s2`. Write a program to create a new string `s3` by appending `s2` in the middle of `s1`.



def append_in_middle(s1, s2):
    middle_index = len(s1) // 2
    s3 = s1[:middle_index] + s2 + s1[middle_index:]
    return s3

# Test the function
s1 = "Hello, World!"
s2 = "Python"
s3 = append_in_middle(s1, s2)
print("Original String s1:", s1)
print("String s2 to append:", s2)
print("New String s3:", s3)
