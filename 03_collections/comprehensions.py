
# 1. WHAT IS A COMPREHENSION?
# A comprehension is a shorter and cleaner way to create:
# - lists
# - dictionaries
# - sets
# - generators
# It is based on a for-loop (and optionally an if-condition).
# It is not magic; it does the same as a normal loop but in a single line.


# 2. LIST COMPREHENSION (for lists)
# Long version (without comprehension):
doubles = []
for x in range(5):            # x takes the values 0, 1, 2, 3, 4
    doubles.append(x * 2)     # append x*2 to the list

# Short version (with list comprehension):
doubles = [x * 2 for x in range(5)]
# Read this as:
# "create a list with x*2 for each x in range(5)"

# Another example with condition (only even numbers):
evens = [x for x in range(10) if x % 2 == 0]
# Meaning:
# "for each x in range(10), if x is even, include it in the list"


# 3. DICT COMPREHENSION (for dictionaries)
# Long version:
squares = {}
for x in range(5):
    squares[x] = x ** 2       # key = x, value = x squared

# Short version:
squares = {x: x ** 2 for x in range(5)}
# Structure:
# {key: value for element in iterable}

# Example with condition (only even x):
even_squares = {x: x ** 2 for x in range(10) if x % 2 == 0}


# 4. SET COMPREHENSION (for sets)
# A set does not allow duplicates.

# Short version:
lengths = {len(word) for word in ["hello", "goodbye", "python", "hello"]}
# It computes the length of each word.
# If a length repeats, the set stores it only once.


# 5. GENERATOR COMPREHENSION (memory efficient)
# Similar to list comprehension, but using parentheses ().
# It does not create the entire list at once; it yields values one by one.

generator_obj = (x * 2 for x in range(5))
# This is NOT a list, it's a generator.

for value in generator_obj:
    print(value)
# Useful when working with large amounts of data and you want to save memory.


# 6. QUICK SUMMARY (MENTAL TEMPLATE)
# List:   [expression for x in iterable if condition]
# Dict:   {key: value for x in iterable if condition}
# Set:    {expression for x in iterable if condition}
# Gen:    (expression for x in iterable if condition)


# 7. FINAL CLEAR EXAMPLE
# Given a list of numbers, we want:
# - a list with their squares (list)
# - a dictionary number -> square (dict)
# - a set with squares of even numbers only (set)

numbers = [1, 2, 3, 4, 5]

squares_list = [n ** 2 for n in numbers]
# [1, 4, 9, 16, 25]

squares_dict = {n: n ** 2 for n in numbers}
# {1:1, 2:4, 3:9, 4:16, 5:25}

squares_even_set = {n ** 2 for n in numbers if n % 2 == 0}
# {4, 16}

# CONCLUSION:
# Comprehensions are simply a shorter and cleaner way
# to write loops that create new data structures.
# If you understand a normal for-loop, a comprehension is the same,
# just written in one line.
