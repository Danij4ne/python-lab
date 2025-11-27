# TUPLES AND LISTS EXERCISES
# Write the code below each exercise.
# No specific functions or methods are indicated: you decide which ones to use.

# PART 1 — TUPLES

# 1) Create a tuple with ten numbers and print:
#    - The fourth element
#    - The elements from the second to the fourth
#    - The last element

my_tuple = (3, 6, 4, 1, 9, 5, 11, 22, 18, 7)

print(my_tuple[3])
print(my_tuple[2:5])
print(my_tuple[-1])

# 2) Create a tuple with different data types (text, number, boolean, etc.) and print:
#    - The first element
#    - The last element
#    - How many times a specific value appears

my_second_tuple = ("Hello", 23, True, 9, "Friend", 293)

print(my_second_tuple[0])
print(my_second_tuple[-1])
print(my_second_tuple.count(23))

# 3) Create a tuple with several numbers and print:
#    - How many elements it has
#    - The largest value
#    - The smallest value
#    - The total sum

my_sum_tuple = (12, 22, 34, 2, 11, 48)

print(len(my_sum_tuple))
print(max(my_sum_tuple))
print(min(my_sum_tuple))
print(sum(my_sum_tuple))

# 4) Given the nested tuple:
NT = (1, 2, ("pop", "rock"), (3, 4, ("disco", (1, 2))))
#    Print:
#      - "rock"
#      - "disco"
#      - The number 2 inside the last group

print(NT[2][1])         # "rock"
print(NT[3][2][0])      # "disco"
print(NT[3][2][1][1])   # 2

# Given the nested tuple:
data = ("Python", (10, 20, ("AI", "ML")), (("Data", (1, 2, 3)), "Science"))
# Print:
#   - "ML"
#   - The number 3
#   - "Data"
#   - "Science"

print(data[1][2][1])        # "ML"
print(data[2][0][1][2])     # 3
print(data[2][0][0])        # "Data"
print(data[2][1])           # "Science"

# 5) Create your own 3-level nested tuple that contains your name inside it.
#    Print only your name.

my_nested_tuple = ("level1", ("level2", ("Dani",)))
print(my_nested_tuple[1][1][0])


# PART 2 — LISTS

# 6) Create a list with three elements and print:
#    - Each element separately
#    - The first two elements
#    - The full list after adding two new values at the end

my_list = ["apple", "banana", "cherry"]

print(my_list[0])
print(my_list[1])
print(my_list[2])

print(my_list[:2])

my_list.append("orange")
my_list.append("grape")
print(my_list)

# 7) Create a list with three numbers.
#    - Append [4, 5] as a single element
#    - Recreate the original list and then add 4 and 5 as individual elements
#    - Write in a comment the difference you see

numbers = [1, 2, 3]
numbers.append([4, 5])
print(numbers)  # [1, 2, 3, [4, 5]] -> the last element is a list

numbers2 = [1, 2, 3]
numbers2.append(4)
numbers2.append(5)
print(numbers2)  # [1, 2, 3, 4, 5] -> all elements are at the same level

# 8) Create a list with some fruit names.
#    Perform the following actions:
#      - Add a new element at the end
#      - Insert an element in the second position
#      - Remove a specific element by value
#      - Remove the last element and print it
#      - Reverse the order of the list

fruits = ["apple", "banana", "orange"]

fruits.append("kiwi")
fruits.insert(1, "mango")   # second position (index 1)
fruits.remove("orange")
last_fruit = fruits.pop()
print(last_fruit)
fruits.reverse()
print(fruits)

# 9) Create a list of numbers and sort it.
#    Then recreate the original list and sort it in a way that does not modify the original.
#    Write in a comment the difference between both approaches.

nums = [5, 2, 9, 1, 7]
nums.sort()
print(nums)  # list is modified in place

nums_original = [5, 2, 9, 1, 7]
nums_sorted = sorted(nums_original)
print(nums_original)  # original list remains unchanged
print(nums_sorted)    # new sorted list


# PART 3 — STRINGS AND CONVERSION

# 10) Create a string with two words separated by a space.
#     Convert the string into a list and print the first word.

text = "Hello world"
words = text.split()
print(words[0])

# 11) Create the string "A, B, C , D"
#     Split it using commas and remove extra spaces.
#     Print the cleaned result.

letters = "A, B, C , D"
parts = [item.strip() for item in letters.split(",")]
print(parts)


# PART 4 — GENERAL REVIEW

# 12) Create a tuple with repeated numbers.
#     Print the position where a specific number appears for the first time
#     and how many times it appears in total.

numbers_tuple = (2, 5, 2, 8, 2, 10, 5)
value = 2
first_index = numbers_tuple.index(value)
count_value = numbers_tuple.count(value)

print(first_index)
print(count_value)

# 13) Create a list with mixed numbers and letters.
#     Create a new list that contains only the numbers, sort it in descending order,
#     and add a word at the end indicating that you finished.

mixed_list = [3, "a", 7, "b", 1, "c", 10]
only_numbers = [item for item in mixed_list if isinstance(item, (int, float))]
only_numbers.sort(reverse=True)
only_numbers.append("done")
print(only_numbers)





















































