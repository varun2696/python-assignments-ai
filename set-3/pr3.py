# 1. **Two Sum Problem**: Given an array of integers and a target integer, find the two integers in the array that sum to the target.
#     - *Input*: [2, 7, 11, 15], target = 9
#     - *Output*: "[0, 1]"



def find_two_sum(nums, target):
    num_to_index = {}  # Dictionary to store the number and its index
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], index]
        num_to_index[num] = index

    return None

# Test the function
nums = [2, 7, 11, 15]
target = 9
result = find_two_sum(nums, target)
print(result)
