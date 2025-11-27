
# Lambda functions
lambda first_value, second_value: first_value + second_value  # anonymous function, no name

# Assign the lambda to a variable to store and call it
sum_two_values = lambda first_value, second_value: first_value + second_value

print(sum_two_values(2, 4))


# =========================================================
# Simple Explanation: map(), filter() and reduce()
# =========================================================

# map()
# Applies an operation to every element in a list.
numbers = [1, 2, 3]
doubles = list(map(lambda x: x * 2, numbers))
print(doubles)  # [2, 4, 6]


# filter()
# Keeps only the elements that satisfy a condition.
numbers = [1, 2, 3, 4]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4]


# reduce()
# Combines all values into a single result.
from functools import reduce
numbers = [1, 2, 3, 4]
total_sum = reduce(lambda a, b: a + b, numbers)
print(total_sum)  # 10


# =========================================================
# Exercises with lambda
# =========================================================

# Exercise 1
# Create a lambda function that subtracts two numbers.

lambda_subtract = lambda n1, n2: n1 - n2
print(lambda_subtract(4, 2))


# Exercise 2
# Use a lambda function to get all numbers greater than 10 from a list.

lister = [12, 8, 10, 9, 22, 39, 1, 40]
greater_than_10 = list(filter(lambda num: num > 10, lister))

print(greater_than_10)


# Exercise 3
# Use a lambda function to convert all names in a list to lowercase.

names_list = ["Pedro", "Londres", "COCO", "CHOCOLATE"]
lowercase_names = list(map(lambda text: text.lower(), names_list))

print(lowercase_names)


# Exercise 4
# Use a lambda function to multiply all numbers in a list.

lista2 = [3, 5, 3, 1, 7, 8, 21, 3, 11]
product = reduce(lambda a, b: a * b, lista2)

print(product)


# Exercise 5
# You have a list of tuples with names and ages.
# Use a lambda function to sort the list by age.

people = [("John", 22), ("Alice", 19), ("Bob", 30), ("Dani", 24)]

sorted_people = sorted(people, key=lambda person: person[1])
print(sorted_people)









