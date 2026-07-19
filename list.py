# A list is a built-in Python data structure used to store multiple items in a single variable.

# Features of Lists:
# Ordered (items have a fixed position)
# Mutable (items can be changed)
# Allows duplicate values
# Can store different data types
# Syntax
from shutil import copy


my_list = [10, 20, 30, 40]

fruits = ["Apple", "Banana", "Mango"]
print(fruits)

# Using index numbers:
fruits = ["Apple", "Banana", "Mango"]
print(fruits[0])
print(fruits[2])

# Negative indexing:
print(fruits[-1])
#slicing
print(fruits[0:2])  # Output: ['Apple', 'Banana']
print(fruits[1:3])   # Output: ['Banana', 'Mango']
print(fruits[-2:-1])   # Output: ['Banana']

# Modifying List Elements
fruits = ["Apple", "Banana", "Mango"]
fruits[1] = "Orange"
print(fruits)

# List Methods
# 1. append():-Adds an item at the end.
numbers = [10, 20, 30]
numbers.append(40)
print(numbers)

# 2. insert():-Adds an element at a specified position.
numbers = [10, 20, 30]
numbers.insert(1, 15)
print(numbers)

# 3. extend():-Adds multiple elements from another list
a = [1, 2]
b = [3, 4]
a.extend(b)
print(a)

# 4. remove():-Removes the first occurrence of a specified value.
numbers = [10, 20, 30, 20]  
numbers.remove(20)
print(numbers)

# 5. pop():-Removes and returns the last item in the list.
numbers = [10, 20, 30]  
numbers.pop(0)
print(numbers)

# 6. clear():-Removes all elements.
numbers = [1, 2, 3]
numbers.clear()
print(numbers)

# 7. index():-Returns the index of a value.
fruits = ["Apple", "Banana", "Mango"]
print(fruits.index("Banana"))

# 8. count():-Counts how many times a value appears.
numbers = [1, 2, 2, 3, 2]
print(numbers.count(2))

# 9. sort():-Sorts the list in ascending order.
numbers = [5, 2, 8, 1]
numbers.sort()
print(numbers)

# Descending order:
numbers.sort(reverse=True)
print(numbers)

# 10. reverse():-Reverses the list.
numbers = [1, 2, 3, 4]
numbers.reverse()
print(numbers)

# 11. copy():-Creates a copy of a list.
a = [10, 20, 30]
b = a.copy()
print(b)


# Loop Through a List
fruits = ["Apple", "Banana", "Mango"]
for fruit in fruits:
    print(fruit)

# Creates a new list in a concise way.
numbers = [1, 2, 3, 4, 5]
squares = [x*x for x in numbers]
print(squares)

# Program 1: Find the Sum of List Elements
numbers = [10, 20, 30, 40]
total = sum(numbers)
print("Sum =", total)

# Program 2: Find the Largest Number
numbers = [12, 45, 67, 23, 89]
largest = max(numbers)
print("Largest =", largest)

# Program 3: Find the Smallest Number
numbers = [12, 45, 67, 23, 89]
smallest = min(numbers)
print("Smallest =", smallest)

# Program 4: Search an Element
numbers = [10, 20, 30, 40]
item = 30
if item in numbers:
    print("Found")
else:
    print("Not Found")

# Program 5: Remove Duplicate Elements
numbers = [1, 2, 2, 3, 4, 4, 5]
unique = list(set(numbers))
print(unique)