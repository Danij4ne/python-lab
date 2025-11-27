
# REVIEW EXERCISES — FUNCTIONS AND LOOPS

# 1) Create a list of numbers and display:
# - How many elements it has
# - The sum of all numbers
# - The smallest number
# - The largest number

my_list = [2, 4, 3, 6, 54, 1, 223, 90]

print(len(my_list))
print(sum(my_list))
print(min(my_list))
print(max(my_list))


# 2) Create a list and sort it in two ways:
# - Into a new sorted list
# - Modifying the original list

new_list = [90, 83, 44, 32, 21, 1, 39, 3, 4, 2, 8, 19]

my_sorted_list = sorted(new_list)
print(my_sorted_list)

new_list.sort()
print(new_list)


# 3) Write a function that adds 1 to a number and returns the result.
# Apply the function to each number in a list and print the results.

other_list = [1, 2, 3, 4, 5]

def add_one(num):
    return num + 1

for n in other_list:
    print(add_one(n))


# 4) Write a function that multiplies two values and returns the result.

def multiply(a, b):
    return a * b

print(multiply(2, 4))


# 5) Create a function that loops through a list and prints the index and the value.

my_go_list = [33, 21, 4, 9, 11, 14]

def print_with_index(lst):
    for idx, value in enumerate(lst):
        print(idx, value)

print_with_index(my_go_list)


# 6) Create a function that receives a variable number of names and prints them one by one.

def print_names(*names):
    for n in names:
        print(n)

print_names("Dani", "Gonzalo", "Pau", "Ivan")


# 7) Create a function that modifies a string inside the function and returns the result.
# Compare the value inside and outside the function.

def to_upper(text):
    text = text.upper()
    return text

print(to_upper("Hello"))


# 8) Define a variable inside a function so it also exists outside it.

def chocolates(coco):
    global choco
    choco = "chocolates"
    coco = coco + choco
    print(coco)

chocolates("hi")
print(choco)


# 9) Create a loop that asks the user for numbers:
# - If the number is 0, stop.
# - If the number is negative, ignore it.
# - If positive, accumulate it.
# - At the end, print the total sum.

sum_num = []

while True:
    number = int(input("Enter a number: "))
    if number == 0:
        break
    elif number < 0:
        pass
    else:
        sum_num.append(number)

print(sum_num)
print("Total:", sum(sum_num))


# 10) Create a loop that asks for text until the user types “exit”.

while True:
    text = input("Type something (or 'exit' to stop): ")
    if text.lower() == "exit":
        break


# 11) Create an empty list and two functions:
# - One to add elements
# - One to remove elements
# Test both and print the final list.

items = []

def add_item(element):
    items.append(element)

def remove_item(element):
    if element in items:
        items.remove(element)

add_item("apple")
add_item("banana")
remove_item("apple")

print(items)


# 12) Create a function that prints numbers from 1 up to a limit.

def printer(start, limit):
    for i in range(start, limit + 1):
        print(i)


# 13) Create a function that returns the n largest values of a list.

def max_numbers(lst, n):
    ordered = sorted(lst, reverse=True)
    return ordered[:n]

numbers = [10, 5, 8, 20, 3, 15]
result = max_numbers(numbers, 3)
print(result)  # [20, 15, 10]

















































