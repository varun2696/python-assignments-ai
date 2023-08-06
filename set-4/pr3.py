# 3. **Longest Common Prefix**: Given a list of strings, find the longest common prefix.
#     - *Input*: ["flower","flow","flight"]
#     - *Output*: "fl"


def longest_common_prefix(strings):
    if not strings:
        return ""

    for i, char in enumerate(strings[0]):
        for string in strings[1:]:
            if i >= len(string) or string[i] != char:
                return strings[0][:i]

    return strings[0]


# Test the function
input_list = ["flower", "flow", "flight"]
result = longest_common_prefix(input_list)
print(result)
