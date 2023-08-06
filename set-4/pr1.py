# 1. **Anagram Check**: Write a Python function that checks whether two given words are anagrams.
#     - *Input*: "cinema", "iceman"
#     - *Output*: "True"


def are_anagrams(word1, word2):
    return sorted(word1.lower()) == sorted(word2.lower())

# Test the function
word1 = "cinema"
word2 = "iceman"
result = are_anagrams(word1, word2)
print(result)
