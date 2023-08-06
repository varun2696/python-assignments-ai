# 7. **Prime Number**: Write a Python function that checks whether a given number is a prime number.
#     - *Input*: 13
#     - *Output*: "13 is a prime number."



def is_prime(number):
    # Check if the number is less than 2
    if number < 2:
        return False

    # Check for factors from 2 to the square root of the number (inclusive)
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False

    return True

# Test the function
num = 17
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
