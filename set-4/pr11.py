# 11. **Binary Search**: Write a function that implements binary search on a sorted array.
#     - *Input*: [1, 2, 3, 4, 5, 6], target = 4
#     - *Output*: "3"


def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# Test the function
input_array = [1, 2, 3, 4, 5, 6]
target_value = 4
result = binary_search(input_array, target_value)
print(result)
