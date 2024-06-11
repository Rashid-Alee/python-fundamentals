# strings_and_file_handling/strings_and_file_handling.py
# Python Strings and File Handling

# String operations and manipulations

# Creating and printing a string
my_string = "Hello, World!"
print("Original String:", my_string)  # Output: Hello, World!

# Accessing characters in a string
print("First character:", my_string[0])  # Output: H
print("Last character:", my_string[-1])  # Output: !

# Slicing a string
print("Substring (0:5):", my_string[0:5])  # Output: Hello
print("Substring (7:):", my_string[7:])  # Output: World!

# String concatenation
greeting = "Hello"
name = "Alice"
full_greeting = greeting + ", " + name + "!"
print("Full Greeting:", full_greeting)  # Output: Hello, Alice!

# String methods
print("Uppercase:", my_string.upper())  # Output: HELLO, WORLD!
print("Lowercase:", my_string.lower())  # Output: hello, world!
print("Title Case:", my_string.title())  # Output: Hello, World!
print(
    "Replace 'World' with 'Python':", my_string.replace("World", "Python")
)  # Output: Hello, Python!
print("Split string:", my_string.split(", "))  # Output: ['Hello', 'World!']

# Checking string properties
print("Is alphanumeric:", my_string.isalnum())  # Output: False
print("Is alphabetic:", my_string.isalpha())  # Output: False
print("Is digit:", my_string.isdigit())  # Output: False

# File handling

# Writing to a file
try:
    with open("example.txt", "w") as file:
        file.write("Hello, World!\n")
        file.write("Welcome to Python file handling.")
    print("File written successfully.")
except IOError as e:
    print("Error writing to file:", e)

# Reading from a file
try:
    with open("example.txt", "r") as file:
        content = file.read()
        print("File content:\n", content)
except IOError as e:
    print("Error reading from file:", e)

# Appending to a file
try:
    with open("example.txt", "a") as file:
        file.write("\nThis line is appended.")
    print("File appended successfully.")
except IOError as e:
    print("Error appending to file:", e)

# Reading line by line
try:
    with open("example.txt", "r") as file:
        for line in file:
            print("Read line:", line.strip())
except IOError as e:
    print("Error reading from file:", e)
