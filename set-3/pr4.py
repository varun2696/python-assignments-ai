# 1. **Palindrome Check**: Write a Python function that checks whether a given word or phrase is a palindrome.
#     - *Input*: "madam"
#     - *Output*: "The word madam is a palindrome."


def is_palindrome(word):
    cleaned_word = ''.join(char.lower() for char in word if char.isalnum())
    reversed_word = cleaned_word[::-1]

    if cleaned_word == reversed_word:
        return True
    else:
        return False

# Test the function
input_word = "madam"
if is_palindrome(input_word):
    print(f"The word {input_word} is a palindrome.")
else:
    print(f"The word {input_word} is not a palindrome.")
