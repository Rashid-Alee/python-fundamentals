# exception_handling/exception_handling.py
# Python Exception Handling: try-except, raising exceptions, and finally

# Example of a try-except block
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Error:", e)  # Output: Error: division by zero

# Handling multiple exceptions
try:
    a = int("Hello")
except ValueError as e:
    print(
        "ValueError:", e
    )  # Output: ValueError: invalid literal for int() with base 10: 'Hello'
except TypeError as e:
    print("TypeError:", e)

# Using else with try-except
try:
    num = int("20")
except ValueError as e:
    print("ValueError:", e)
else:
    print("Conversion successful, num:", num)  # Output: Conversion successful, num: 20

# Using finally for cleanup actions
try:
    f = open("testfile.txt", "w")
    f.write("Hello, world!")
except IOError as e:
    print("IOError:", e)
finally:
    f.close()
    print("File closed.")  # Output: File closed.

# Raising exceptions
try:
    age = -5
    if age < 0:
        raise ValueError("Age cannot be negative")
except ValueError as e:
    print("Error:", e)  # Output: Error: Age cannot be negative


# Custom exceptions
class CustomError(Exception):
    pass


try:
    raise CustomError("This is a custom error")
except CustomError as e:
    print("CustomError:", e)  # Output: CustomError: This is a custom error
