# Tuples (immutable, cannot be changed)

my_tuple = (10, 2, 4, 5, 67, 4, 87, 33, 25, 6)

print(my_tuple[4])

diverse_tuple = ("Hello", 4, 5, 5.3, True, 94, "Dani")

print(diverse_tuple[0])

tuple1 = my_tuple + diverse_tuple  # concatenate the two tuples

print(tuple1)

tuple1 = tuple1 + ("Cool", 70, False)  # add more values to the tuple

print(tuple1)

print(tuple1[1:4])  # elements from index 1 to 3

# sorted() -> sort values from smallest to largest
# tuple1 = sorted(tuple1) -> ERROR because this tuple contains booleans and strings

my_new_tuple = (5, 7, 32, 1, 3, 2, 5, 77, 4)

my_new_tuple = sorted(my_new_tuple)  # sort the tuple (result is a list)

print(my_new_tuple)

# Nesting -> a tuple can contain other tuples inside it
# putting one structure inside another

# Example 1: one tuple with 3 inner tuples (all at the same level)
my_tuple2 = (1, 5, 4, 3), (38, 22, 9, 21), (83, 88, 73, 77)

print(my_tuple2[0])      # (1, 5, 4, 3)
print(my_tuple2[0][0])   # 1

print(my_tuple2[1])      # (38, 22, 9, 21)
print(my_tuple2[2])      # (83, 88, 73, 77)

print(my_tuple2)

# Example 2: single main tuple that contains different element types,
# including tuples nested at different levels

NT = (1, 2, ("pop", "rock"), (3, 4, ("disco", (1, 2))))

print(NT[0])         # 1
print(NT[1])         # 2
print(NT[2])         # ("pop", "rock")

print(NT[2][0])      # "pop"
print(NT[2][1])      # "rock"

print(NT[3])         # (3, 4, ("disco", (1, 2)))
print(NT[3][2][0])   # "disco"

# Visual “tree” of the tuple, showing nesting levels
"""
NT
├── 1
├── 2
├── ("pop", "rock")
│    ├── "pop"
│    └── "rock"
└── (3, 4, ("disco", (1, 2)))
     ├── 3
     ├── 4
     └── ("disco", (1, 2))
           ├── "disco"
           └── (1, 2)
                ├── 1
                └── 2
"""

# Level 1 → main elements inside NT:
# 1
# 2
# ("pop", "rock")
# (3, 4, ("disco", (1, 2)))

# Level 2 → inside ("pop", "rock"):
#   "pop"
#   "rock"

# Level 2 → inside (3, 4, ("disco", (1, 2))):
#   3
#   4
#   ("disco", (1, 2))

# Level 3 → inside ("disco", (1, 2)):
#   "disco"
#   (1, 2)

# Level 4 → inside (1, 2):
#   1
#   2

# Lists -> mutable and ordered; in many cases they behave similarly to tuples,
# but the main difference is that lists can be modified and tuples cannot.

my_list = ["Michael Jackson", 10.1, 1982]

print(my_list[0])
print(my_list[1])
print(my_list[2])

# Slices also work with lists

print(my_list[0:2])  # "Michael Jackson", 10.1

# Concatenate lists
my_new_list = my_list + ["pop", 10]
print(my_new_list)

# .append(x) → add a single element at the end
my_list = [1, 2, 3]
my_list.append([4, 5])
print(my_list)       # [1, 2, 3, [4, 5]]
print(my_list[3])    # [4, 5]

# .extend(iterable) → add all elements of the iterable one by one
my_list = [1, 2, 3]
my_list.extend([4, 5])
print(my_list)       # [1, 2, 3, 4, 5]

# Modify list elements
#      0         1     2
A = ["disco", 10, 1.2]

A[0] = "Hard Rock"  # replace element at index 0

print(A)            # ["Hard Rock", 10, 1.2]

# del (delete by index)
del A[2]            # delete element at index 2 -> 1.2

print(A)            # ["Hard Rock", 10]

# Convert string to list (split)
my_rock = "Hard rock"

my_rock = my_rock.split()

print(my_rock)  # ["Hard", "rock"] -> now a list with two elements

# Using split to split strings
vocabulary = "A, B, C , D"

vocabulary = vocabulary.split(",")  # split by commas and create a list
print(vocabulary)

# append vs extend

shopping_list = ["Milk", "Eggs", "Bread"]

# append() → adds one single element
shopping_list.append("Football")
print(shopping_list)
# ["Milk", "Eggs", "Bread", "Football"]

# extend() → adds multiple elements from another iterable
shopping_list.extend(["Juice", "Apples"])
print(shopping_list)
# ["Milk", "Eggs", "Bread", "Football", "Juice", "Apples"]

# If you use extend with a string, it adds character by character
shopping_list.extend("Ball")
print(shopping_list)
# ["Milk", "Eggs", "Bread", "Football", "Juice", "Apples", "B", "a", "l", "l"]

# How to sort a tuple (which is immutable)?
# sort() → works only with lists, sorts in place, returns nothing, modifies the original
# sorted() → works with any iterable, does not modify the original, returns a new sorted list

ranking = (0, 9, 6, 5, 10, 8, 9, 6, 2)

ranking_sorted = sorted(ranking)
print(ranking_sorted)

# List functions

fruits = ["apple", "banana", "cherry"]

# append() → add element to the end
fruits.append("orange")
print(fruits)  # ["apple", "banana", "cherry", "orange"]

# copy() → create an independent copy of the list
new_fruits = fruits.copy()
print(new_fruits)  # ["apple", "banana", "cherry", "orange"]

# count() → count how many times a value appears
print(fruits.count("apple"))  # 1

# del → delete element by index
del fruits[1]
print(fruits)  # ["apple", "cherry", "orange"]

# extend() → add multiple elements from another list
fruits.extend(["kiwi", "mango"])
print(fruits)  # ["apple", "cherry", "orange", "kiwi", "mango"]

# insert() → insert element at a specific position
fruits.insert(1, "banana")
print(fruits)  # ["apple", "banana", "cherry", "orange", "kiwi", "mango"]

# pop() → remove and return last element (or element at given index)
fruits.pop()
print(fruits)  # ["apple", "banana", "cherry", "orange", "kiwi"]

# remove() → remove first occurrence of a value
fruits.remove("banana")
print(fruits)  # ["apple", "cherry", "orange", "kiwi"]

# reverse() → reverse list order
fruits.reverse()
print(fruits)  # ["kiwi", "orange", "cherry", "apple"]

# sort() → sort list (alphabetically or numerically)
fruits.sort()
print(fruits)  # ["apple", "cherry", "kiwi", "orange"]

# Tuples

# Tuples are immutable (cannot be modified)
numbers = (5, 2, 8, 2, 10, 6)

# count() → how many times a value appears
print(numbers.count(2))  # 2

# index() → index (position) of the first occurrence of a value
print(numbers.index(8))  # 2

# sum() → sum of all numeric values
print(sum(numbers))      # 33

# min() and max() → minimum and maximum values
print(min(numbers))      # 2
print(max(numbers))      # 10

# len() → number of elements
print(len(numbers))      # 6

# Example note:
# player_attributes = default_attributes[:]  # creates an exact copy of the list
