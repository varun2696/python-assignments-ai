# Problem 9: Create a dictionary by extracting the keys from a given dictionary
# Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.
# Given dictionary:
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}

# # Keys to extract
# keys = ["name", "salary"]



sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New York"
}

keys_to_extract = ["name", "salary"]

# Create a new dictionary with the extracted keys
new_dict = {key: sample_dict[key] for key in keys_to_extract}

print(new_dict)
