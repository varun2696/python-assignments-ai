# 4. **String Permutations**: Write a Python function to calculate all permutations of a given string.
#     - *Input*: "abc"
#     - *Output*: "['abc', 'acb', 'bac', 'bca', 'cab', 'cba']"


def permutations(s):
    if len(s) == 1:
        return [s]

    result = []
    for i in range(len(s)):
        prefix = s[i]
        rest = s[:i] + s[i+1:]
        sub_permutations = permutations(rest)
        for perm in sub_permutations:
            result.append(prefix + perm)

    return result


# Test the function
input_string = "abc"
result = permutations(input_string)
print(result)
