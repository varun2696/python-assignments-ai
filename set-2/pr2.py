# ### Problem **2: Display numbers from a list using loop**

# Write a program to display only those numbers from a [list](https://pynative.com/python-lists/) that satisfy the following conditions

# - The number must be divisible by five
# - If the number is greater than 150, then skip it and move to the next number
# - If the number is greater than 500, then stop the loop


def display_numbers(numbers_list):
    for number in numbers_list:
        if number % 5 == 0:
            if number > 500:
                break
            elif number > 150:
                continue
            else:
                print(number)

# Test the function
numbers_list = [45, 55, 160, 200, 505, 120, 250, 480, 510]
display_numbers(numbers_list)
