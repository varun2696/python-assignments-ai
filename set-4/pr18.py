# 18. **Maximum Subarray**: Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
#     - *Input*: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
#     - *Output*: "6"


def max_subarray_sum(nums):
    max_sum = nums[0]
    current_sum = nums[0]

    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)

    return max_sum


# Test the function
input_array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
output = max_subarray_sum(input_array)
print(output)
