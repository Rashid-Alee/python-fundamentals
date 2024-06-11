# Python Control Flow: if-else statements and loops

# if-else statements
num = 10

if num > 0:
    print(f"{num} is a positive number")  # Output: 10 is a positive number
elif num == 0:
    print(f"{num} is zero")  # This won't execute
else:
    print(f"{num} is a negative number")  # This won't execute

# for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Output:
# apple
# banana
# cherry

# range() function with for loop
for i in range(5):
    print(i)
# Output:
# 0
# 1
# 2
# 3
# 4

# while loop
count = 0
while count < 5:
    print("Count:", count)
    count += 1
# Output:
# Count: 0
# Count: 1
# Count: 2
# Count: 3
# Count: 4

# break statement
for i in range(10):
    if i == 5:
        break
    print(i)
# Output:
# 0
# 1
# 2
# 3
# 4

# continue statement
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
# Output:
# 1
# 3
# 5
# 7
# 9
