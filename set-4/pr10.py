# 10. **Contains Duplicate**: Given an array of integers, find if the array contains any duplicates.
#     - *Input*: [1, 2, 3, 1]
#     - *Output*: "True"


# You can find if an array contains any duplicates by using a set to keep track of the elements you have seen so far.


def contains_duplicate(nums):
    num_set = set()

    for num in nums:
        if num in num_set:
            return True
        num_set.add(num)

    return False


# Test the function
input_array = [1, 2, 3, 1]
result = contains_duplicate(input_array)
print(result)
