# 6. **Missing Number**: Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
#     - *Input*: [3, 0, 1]
#     - *Output*: "2"


def find_missing_number(nums):
    n = len(nums)
    xor_result = 0

    # XOR all the elements in the given array
    for num in nums:
        xor_result ^= num

    # XOR the result with all numbers from 0 to n
    for i in range(n + 1):
        xor_result ^= i

    return xor_result


# Test the function
input_array = [3, 0, 1]
result = find_missing_number(input_array)
print(result)
