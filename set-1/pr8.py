# 8. **Factorial Calculation**: Write a Python function that calculates the factorial of a number.
#     - *Input*: 5
#     - *Output*: "Factorial of 5 is 120."



def factorial(number):
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif number == 0:
        return 1
    else:
        result = 1
        for i in range(1, number + 1):
            result *= i
        return result

# Test the function
num = 5
print(f"The factorial of {num} is: {factorial(num)}")
