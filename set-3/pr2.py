# 1. **Dictionary Manipulation**: Create a dictionary with keys as names and values as ages. Write functions to add a new name-age pair, update the age of a name, and delete a name from the dictionary.
#     - *Input*: Add "John": 25, Update "John": 26, Delete "John"
#     - *Output*: "{}, {'John': 26}, {}"



def add_person(dictionary, name, age):
    dictionary[name] = age

def update_age(dictionary, name, new_age):
    if name in dictionary:
        dictionary[name] = new_age
    else:
        print(f"Name '{name}' not found in the dictionary.")

def delete_person(dictionary, name):
    if name in dictionary:
        del dictionary[name]
    else:
        print(f"Name '{name}' not found in the dictionary.")

# Test the functions
person_dict = {}

add_person(person_dict, "John", 25)
print(person_dict)

update_age(person_dict, "John", 26)
print(person_dict)

delete_person(person_dict, "John")
print(person_dict)
