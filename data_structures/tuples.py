# data_structures/tuples.py
# Python Tuples: Creation, Access, and Immutability

# Creating a tuple
colors = ("red", "green", "blue")
print("Initial tuple:", colors)  # Output: ("red", "green", "blue")

# Accessing elements
print("First color:", colors[0])  # Output: "red"
print("Last color:", colors[-1])  # Output: "blue"

# Tuples are immutable
try:
    colors[0] = "yellow"
except TypeError as e:
    print("Error:", e)  # Output: 'tuple' object does not support item assignment

# Tuple packing and unpacking
point = (1, 2)
x, y = point
print("x:", x)  # Output: 1
print("y:", y)  # Output: 2
