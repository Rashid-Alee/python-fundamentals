# data_structures/dictionaries.py
# Python Dictionaries: Creation, Access, and Methods

# Creating a dictionary
student = {"name": "John", "age": 25, "course": "Computer Science"}
print(
    "Initial dictionary:", student
)  # Output: {'name': 'John', 'age': 25, 'course': 'Computer Science'}

# Accessing elements
print("Student name:", student["name"])  # Output: "John"
print("Student age:", student.get("age"))  # Output: 25

# Adding elements
student["grade"] = "A"
print(
    "Dictionary after adding grade:", student
)  # Output: {'name': 'John', 'age': 25, 'course': 'Computer Science', 'grade': 'A'}

# Removing elements
del student["age"]
print(
    "Dictionary after deleting age:", student
)  # Output: {'name': 'John', 'course': 'Computer Science', 'grade': 'A'}

# Iterating over dictionary
for key, value in student.items():
    print(f"{key}: {value}")
# Output:
# name: John
# course: Computer Science
# grade: A
