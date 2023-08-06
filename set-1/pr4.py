# 4. **Sum and Average**: Write a Python program that calculates and prints the sum and average of a list of numbers.
#     - *Input*: [10, 20, 30, 40]
#     - *Output*: "Sum: 100, Average: 25.0"


def calculate_sum(numbers_list):
    # Calculate the sum of numbers in the list
    total_sum = sum(numbers_list)
    return total_sum

def calculate_average(numbers_list):
    # Calculate the average of numbers in the list
    total_sum = sum(numbers_list)
    num_elements = len(numbers_list)
    average = total_sum / num_elements
    return average

def main():
    # Input list of numbers
    numbers_list = [12, 34, 56, 78, 90]

    # Calculate and print the sum
    total_sum = calculate_sum(numbers_list)
    print("Sum of the numbers:", total_sum)

    # Calculate and print the average
    average = calculate_average(numbers_list)
    print("Average of the numbers:", average)

if __name__ == "__main__":
    main()
