# 14. **Quick Sort**: Implement quick sort in Python.
#     - *Input*: [10, 7, 8, 9, 1, 5]
#     - *Output*: "[1, 5, 7, 8, 9, 10]"


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


# Test the function
input_list = [10, 7, 8, 9, 1, 5]
output = quick_sort(input_list)
print(output)
