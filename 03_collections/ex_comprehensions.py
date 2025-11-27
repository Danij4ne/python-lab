# -------------------------------------------
# COMPREHENSIONS EXERCISES
# -------------------------------------------

# Level 1 - Basic (List Comprehensions)

# 1. Create a list with numbers from 0 to 9 using list comprehension.
my_list = [i for i in range(0, 9 + 1)]
print(my_list)

# 2. Create a list with the squares of numbers from 1 to 10.
my_square_list = [i**2 for i in range(1, 10 + 1)]
print(my_square_list)

# 3. Create a list with the even numbers from 0 to 20.
even_list = [i for i in range(21) if i % 2 == 0]
print(even_list)

# 4. Create a list with numbers from 0 to 10 multiplied by 3.
triple_list = [i * 3 for i in range(11)]
print(triple_list)

# 5. Create a list with the letters of the word "python" in uppercase.
upper_list = [i.upper() for i in "python"]
print(upper_list)


# Level 2 - Filtering with Conditions

# 6. From a list of numbers 0 to 20, create a new list with only multiples of 5.
mult_5 = [i for i in range(21) if i % 5 == 0]
print(mult_5)

# 7. From the list ["perro", "gato", "elefante", "sol", "luna"],
#    create another list with words longer than 4 letters.
animal_list = ["perro", "gato", "elefante", "sol", "luna"]
long_words = [word for word in animal_list if len(word) > 4]
print(long_words)

# 8. Create a list with numbers from 1 to 30,
#    but include only those that are odd and multiples of 3.
filtered_list = [i for i in range(31) if i % 2 != 0 and i % 3 == 0]
print(filtered_list)

# 9. Create a list with the squares of numbers from 1 to 10,
#    but only if the square is less than 50.
less_50 = [i**2 for i in range(11) if i**2 < 50]
print(less_50)

# 10. From the sentence "Hola mundo desde Python",
#     create a list with only the words starting with "P" or "p".
python_words = [word for word in "Hola mundo desde Python".split() if word.startswith(("p", "P"))]
print(python_words)


# Level 3 - Dict Comprehensions

# 11. Create a dictionary with keys 1 to 5 and values as their squares.
my_dict = {i: i**2 for i in range(1, 6)}
print(my_dict)

# 12. Create a dictionary where the keys are names
#     ["Ana", "Luis", "Pedro"] and the values are the name lengths.
name_list = ["Ana", "Luis", "Pedro"]
names_dict = {name: len(name) for name in name_list}
print(names_dict)

# 13. Create a dictionary with numbers 1 to 10 as keys
#     and "Even" or "Odd" as values depending on the number.
even_odd_dict = {i: ("Even" if i % 2 == 0 else "Odd") for i in range(1, 11)}
print(even_odd_dict)

# 14. From the dictionary {"a": 1, "b": 2, "c": 3, "d": 4},
#     create another dictionary keeping only keys whose value is even.
base_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
even_values_dict = {k: v for k, v in base_dict.items() if v % 2 == 0}
print(even_values_dict)

# 15. Convert a list of tuples [("name", "Ana"), ("age", 25)]
#     into a dictionary using comprehension.
tuple_list = [("name", "Ana"), ("age", 25)]
tuple_dict = {k: v for k, v in tuple_list}
print(tuple_dict)


# Level 4 - Set Comprehensions

# 16. Create a set with squares of numbers from 0 to 10.
square_set = {i**2 for i in range(11)}
print(square_set)

# 17. From the list ["python", "java", "python", "c++", "java"],
#     create a set with unique languages.
languages = ["python", "java", "python", "c++", "java"]
unique_languages = {lang for lang in languages}
print(unique_languages)

# 18. Create a set with the unique lengths of words
#     in ["sol", "luna", "estrella", "sol", "mar"].
word_list = ["sol", "luna", "estrella", "sol", "mar"]
length_set = {len(word) for word in word_list}
print(length_set)


# Level 5 - Combined and Advanced Comprehensions

# 19. Create a dictionary where keys are numbers from 1 to 5
#     and values are lists of their multiples up to 3.
#     Example: {1: [1,2,3], 2: [2,4,6], ...}
multiples_dict = {i: [i * j for j in range(1, 4)] for i in range(1, 6)}
print(multiples_dict)

# 20. From the list ["ana", "PEDRO", "Juan", "maria"],
#     create a dictionary where keys are lowercase names
#     and values are the names in uppercase.
names = ["ana", "PEDRO", "Juan", "maria"]
name_format_dict = {name.lower(): name.upper() for name in names}
print(name_format_dict)
