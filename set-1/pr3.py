# 3. **List Operations**: Write a Python program to create a list of numbers from 1 to 10, and then add a number, remove a number, and sort the list.
#     - *Input*: None
#     - *Output*: "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20]..."


def main():
    # Create a list of numbers from 1 to 10
    numbers_list = list(range(1, 11))

    # Print the initial list
    print("Initial List:", numbers_list)

    # Add a number to the list
    add_number = 11
    numbers_list.append(add_number)
    print("List after adding", add_number, ":", numbers_list)

    # Remove a number from the list
    remove_number = 3
    if remove_number in numbers_list:
        numbers_list.remove(remove_number)
        print("List after removing", remove_number, ":", numbers_list)
    else:
        print(remove_number, "is not in the list. Cannot remove.")

    # Sort the list
    numbers_list.sort()
    print("Sorted List:", numbers_list)

if __name__ == "__main__":
    main()
