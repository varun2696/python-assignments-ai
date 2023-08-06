# Problem 8: Initialize dictionary with default values
# In Python, we can initialize the keys with the same values.
# Given:
# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}


employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

# Initialize the dictionary with default values
employee_data = {employee: defaults for employee in employees}

print(employee_data)
