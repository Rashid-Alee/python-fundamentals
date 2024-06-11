# Python Variables and Basic Syntax

# Variable assignment
x = 5  # Assigning value 5 to variable x
y = 10  # Assigning value 10 to variable y

# Print the variables
print("Value of x:", x)  # Output: Value of x: 5
print("Value of y:", y)  # Output: Value of y: 10

# Arithmetic operations
sum_xy = x + y  # Adding x and y
difference_xy = x - y  # Subtracting y from x
product_xy = x * y  # Multiplying x and y
quotient_xy = x / y  # Dividing x by y

# Print the results of arithmetic operations
print("Sum of x and y:", sum_xy)  # Output: Sum of x and y: 15
print("Difference of x and y:", difference_xy)  # Output: Difference of x and y: -5
print("Product of x and y:", product_xy)  # Output: Product of x and y: 50
print("Quotient of x and y:", quotient_xy)  # Output: Quotient of x and y: 0.5

# String concatenation
name = "John"  # Assigning string value to variable name
greeting = "Hello, " + name + "!"  # Concatenating strings
print(greeting)  # Output: Hello, John!

# Boolean operations
a = True  # Assigning boolean value True to variable a
b = False  # Assigning boolean value False to variable b
print("a and b:", a and b)  # Output: a and b: False
print("a or b:", a or b)  # Output: a or b: True
print("not a:", not a)  # Output: not a: False

# Comparison operators
print("Is x equal to y?", x == y)  # Output: Is x equal to y? False
print("Is x not equal to y?", x != y)  # Output: Is x not equal to y? True
print("Is x greater than y?", x > y)  # Output: Is x greater than y? False
print(
    "Is x less than or equal to y?", x <= y
)  # Output: Is x less than or equal to y? True

# Identity operators
list1 = [1, 2, 3]  # Assigning a list to variable list1
list2 = [1, 2, 3]  # Assigning another list with same values to variable list2
print("Are list1 and list2 the same object?", list1 is list2)  # Output: False
print("Are list1 and list2 not the same object?", list1 is not list2)  # Output: True

# Membership operators
print("Is 1 in list1?", 1 in list1)  # Output: True
print("Is 4 not in list1?", 4 not in list1)  # Output: True
