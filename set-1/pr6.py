# 6. **Count Vowels**: Write a Python program that counts the number of vowels in a given string.
#     - *Input*: "Hello"
#     - *Output*: "Number of vowels: 2"



def count_vowels(input_string):
    # Define a set of vowels to check against
    vowels = set("aeiouAEIOU")

    # Initialize a counter for vowels
    vowel_count = 0

    # Iterate through the characters in the input string
    for char in input_string:
        if char in vowels:
            vowel_count += 1

    return vowel_count

def main():
    # Input string
    input_string = "Hello, Python!"

    # Call the function to count vowels
    num_vowels = count_vowels(input_string)

    # Print the result
    print("Number of vowels in the string:", num_vowels)

if __name__ == "__main__":
    main()
