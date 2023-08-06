# 15. **Single Number**: Given a non-empty array of integers, every element appears twice except for one. Find that single one.
#     - *Input*: [4,1,2,1,2]
#     - *Output*: "4"


def find_single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result


# Test the function
input_array = [4, 1, 2, 1, 2]
result = find_single_number(input_array)
print(result)
