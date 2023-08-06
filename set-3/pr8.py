# 1. **File I/O**: Write a Python program that reads a file, counts the number of words, and writes the count to a new file.
#     - *Input*: A text file named "input.txt" with the content "Hello world"
#     - *Output*: A text file named "output.txt" with the content "Number of words: 2"




def count_words(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            word_count = len(content.split())
            return word_count
    except FileNotFoundError:
        return -1

def write_count_to_file(file_path, word_count):
    with open(file_path, 'w') as file:
        file.write(f"Number of words: {word_count}")

# Test the program
input_file = "input.txt"
output_file = "output.txt"

word_count = count_words(input_file)
if word_count >= 0:
    write_count_to_file(output_file, word_count)
    print("Word count written to 'output.txt'")
else:
    print("Input file 'input.txt' not found.")



# Before running this program, make sure you have the "input.txt" file with the content "Hello world" in the same directory as the Python script.

# When you run this Python program, it will create a new file named "output.txt" with the content "Number of words: 2". The program reads the content of "input.txt", counts the number of words in it, and then writes the word count to "output.txt".

# If the "input.txt" file is not found, the program will print the message "Input file 'input.txt' not found."