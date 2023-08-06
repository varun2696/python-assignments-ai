# 9. **Power of Two**: Given an integer, write a function to determine if it is a power of two.
#     - *Input*: 16
#     - *Output*: "True"


# You can determine if an integer is a power of two by checking if it has exactly one bit set (i.e., it is a power of two) using bitwise operations.


def is_power_of_two(n):
    if n <= 0:
        return False

    return n & (n - 1) == 0


# Test the function
num = 16
result = is_power_of_two(num)
print(result)
