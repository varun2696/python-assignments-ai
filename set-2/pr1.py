# Write a program to print the following number pattern using a loop.

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5


def print_number_pattern(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

# Test the function
num_rows = 5
print_number_pattern(num_rows)
