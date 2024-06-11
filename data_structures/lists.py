# data_structures/lists.py
# Python Lists: Creation, Operations, and Methods

# Creating a list
fruits = ["apple", "banana", "cherry"]
print("Initial list:", fruits)  # Output: ["apple", "banana", "cherry"]

# Accessing elements
print("First fruit:", fruits[0])  # Output: "apple"
print("Last fruit:", fruits[-1])  # Output: "cherry"

# Adding elements
fruits.append("orange")
print("List after append:", fruits)  # Output: ["apple", "banana", "cherry", "orange"]

# Inserting elements
fruits.insert(1, "mango")
print(
    "List after insert:", fruits
)  # Output: ["apple", "mango", "banana", "cherry", "orange"]

# Removing elements
fruits.remove("banana")
print("List after remove:", fruits)  # Output: ["apple", "mango", "cherry", "orange"]

# Slicing a list
print("Sliced list:", fruits[1:3])  # Output: ["mango", "cherry"]

# List comprehensions
squared_numbers = [x**2 for x in range(5)]
print("Squared numbers:", squared_numbers)  # Output: [0, 1, 4, 9, 16]
