# data_structures/sets.py
# Python Sets: Creation, Operations, and Methods

# Creating a set
numbers = {1, 2, 3, 4, 5}
print("Initial set:", numbers)  # Output: {1, 2, 3, 4, 5}

# Adding elements
numbers.add(6)
print("Set after add:", numbers)  # Output: {1, 2, 3, 4, 5, 6}

# Removing elements
numbers.remove(3)
print("Set after remove:", numbers)  # Output: {1, 2, 4, 5, 6}

# Set operations
evens = {2, 4, 6, 8}
print("Union:", numbers | evens)  # Output: {1, 2, 4, 5, 6, 8}
print("Intersection:", numbers & evens)  # Output: {2, 4, 6}
print("Difference:", numbers - evens)  # Output: {1, 5}
print("Symmetric Difference:", numbers ^ evens)  # Output: {1, 5, 8}
