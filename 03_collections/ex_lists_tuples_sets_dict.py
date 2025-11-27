# EXERCISES — TUPLES, LISTS, DICTIONARIES AND SETS (NO HINTS)
# Copy this block into your .py file and complete each exercise.
# No functions or methods are indicated: you decide how to solve each task.

# 1) TUPLES — BASICS
# 1.1 Create a tuple with these values: (10, 2, 4, 5, 67, 4, 87, 33, 25, 6).
#     Print the 5th element.

my_tuple = (10, 2, 4, 5, 67, 4, 87, 33, 25, 6)
print(my_tuple[4])

# 1.2 Create a tuple with mixed values: ("Hola", 4, 5, 5.3, True, 94, "Dani").
#     Print the first element.

my_second_tuple = ("Hola", 4, 5, 5.3, True, 94, "Dani")
print(my_second_tuple[0])

# 1.3 Join both previous tuples into a new tuple and print it.

my_new_tuple = my_tuple + my_second_tuple
print(my_new_tuple)

# 1.4 Add "Cool", 70 and False to the resulting tuple and print it again.

my_new_tuple += ("Cool", 70, False)
print(my_new_tuple)

# 1.5 Print a slice from index 1 to 3 (not including 4).

print(my_new_tuple[1:4])


# 2) TUPLES — LEVELS AND NESTING
# 2.1 Create a tuple with 3 inner tuples:
#     (1, 5, 4, 3), (38, 22, 9, 21), (83, 88, 73, 77).
#     Print: the first tuple, its first element, the second tuple, the third tuple, and the full structure.

nested_tuple = (1, 5, 4, 3), (38, 22, 9, 21), (83, 88, 73, 77)
print(nested_tuple[0])
print(nested_tuple[0][0])
print(nested_tuple[1])
print(nested_tuple[2])
print(nested_tuple)

# 2.2 Create:
#     NT = (1, 2, ("pop","rock"), (3, 4, ("disco", (1, 2))))
#     Print exactly:
#     1, 2, ("pop","rock"), "pop", "rock", (3, 4, ("disco",(1,2))), "disco".

NT = (1, 2, ("pop", "rock"), (3, 4, ("disco", (1, 2))))
print(NT[0])
print(NT[1])
print(NT[2])
print(NT[2][0])
print(NT[2][1])
print(NT[3])
print(NT[3][2][0])


# 3) TUPLES — NUMERIC OPERATIONS
# 3.1 With the tuple (5, 7, 32, 1, 3, 2, 5, 77, 4):
#     Print the number of elements, the sum, the minimum and the maximum.

t = (5, 7, 32, 1, 3, 2, 5, 77, 4)
print(len(t))
print(sum(t))
print(min(t))
print(max(t))

# 3.2 Print how many times 5 appears and the index of its first appearance.

print(t.count(5))
print(t.index(5))


# 4) LISTS — BASICS
# 4.1 Create the list ["Michael Jackson", 10.1, 1982] and print each element separately.

info = ["Michael Jackson", 10.1, 1982]
print(info[0])
print(info[1])
print(info[2])

# 4.2 Print a slice containing the first two elements.

print(info[:2])

# 4.3 Concatenate that list with ["pop", 10] and print the result.

info += ["pop", 10]
print(info)

# 4.4 Start from [1, 2, 3], append [4, 5] as a single element and print it.
#     Then print the last element.

numbers = [1, 2, 3]
numbers.append([4, 5])
print(numbers)
print(numbers[-1])

# 4.5 Start from [1, 2, 3], append 4 and 5 as individual elements and print it.

numbers = [1, 2, 3]
numbers.append(4)
numbers.append(5)
print(numbers)


# 5) LISTS — MODIFY, DELETE, CONVERT
# 5.1 With ["disco", 10, 1.2], replace "disco" with "Hard Rock" and print it.
# 5.2 Delete the element at index 2 and print the list.
# 5.3 Convert "Hard rock" into a list of two words and print it.
# 5.4 Split "A, B, C , D" by commas into a list and print it.
# 5.5 With ["Milk","Eggs","Bread"], add "Football" as a single element,
#     then add "Juice" and "Apples" as individual elements, and print it.
# 5.6 Reverse the list and print it.
# 5.7 Sort the list alphabetically and print it.

music_list = ["disco", 10, 1.2]
music_list[0] = "Hard Rock"
print(music_list)

del music_list[2]
print(music_list)

hard_rock_text = "Hard rock"
hard_rock_list = hard_rock_text.split()
print(hard_rock_list)

letters_text = "A, B, C , D"
letters_list = [item.strip() for item in letters_text.split(",")]
print(letters_list)

shopping = ["Milk", "Eggs", "Bread"]
shopping.append("Football")
shopping.extend(["Juice", "Apples"])
print(shopping)

shopping.reverse()
print(shopping)

shopping_sorted = sorted(shopping)
print(shopping_sorted)


# 6) LISTS — RANKING
# 6.1 From the tuple (0, 9, 6, 5, 10, 8, 9, 6, 2) create a sorted structure
#     from smallest to largest without modifying the original and print it.

ranking_tuple = (0, 9, 6, 5, 10, 8, 9, 6, 2)
ranking_sorted = sorted(ranking_tuple)
print(ranking_sorted)


# 7) DICTIONARIES — BASICS
# 7.1 Create {"Nombre":"Dani", "Apodo":"Danij"} and print the value of "Nombre".

dicct = {"Nombre": "Dani", "Apodo": "Danij"}
print(dicct["Nombre"])

# 7.2 Add "Amigo":"Antonio" and print it.

dicct["Amigo"] = "Antonio"
print(dicct)

# 7.3 Delete "Amigo" and print the dictionary.

dicct.pop("Amigo")
print(dicct)

# 7.4 Check if "Nombre" exists and print the boolean.

print("Nombre" in dicct)

# 7.5 Print all keys.

print(dicct.keys())

# 7.6 Print all values.

print(dicct.values())


# 8) DICTIONARIES — MIXED TYPES
# 8.1 Create {"A":1, "B":"2", "C":[3,3,3], "D":(4,4,4), "E":5, "F":6}.
#     Print the values of "C" and "D". Change the first value in "C" to 9 and print it.

num_dict = {"A": 1, "B": "2", "C": [3, 3, 3], "D": (4, 4, 4), "E": 5, "F": 6}
print(num_dict["C"])
print(num_dict["D"])

num_dict["C"][0] = 9
print(num_dict["C"])

# 8.2 Try to change the first value in "D" to 9 and handle the error
#     without stopping the program. Then print an explanation.

try:
    num_dict["D"][0] = 9
except TypeError as e:
    print("Cannot modify 'D' because tuples are immutable.")
    print("Error message:", e)


# 9) SETS — BASICS
# 9.1 Create {"Dani","rock","Pokemon","Vampiro","rock","chocolate"} and print it.

my_set = {"Dani", "rock", "Pokemon", "Vampiro", "rock", "chocolate"}
print(my_set)

# 9.2 Check if "Dani" is inside and print the boolean.

print("Dani" in my_set)

# 9.3 Add "cake", print the set, remove it, and print again.

my_set.add("cake")
print(my_set)
my_set.remove("cake")
print(my_set)


# 10) SETS — SET RELATIONSHIPS
# 10.1 Create a = {1,2,3} and b = {1,2,3,4,5}. Check if a is a subset of b
#      and if b is a subset of a, and print both booleans.

a = {1, 2, 3}
b = {1, 2, 3, 4, 5}
print(a.issubset(b))
print(b.issubset(a))

# 10.2 With a = {1,2,3} and b = {3,4,5}, print:
#      common elements, elements only in a, elements only in b, and the union.

a = {1, 2, 3}
b = {3, 4, 5}

common_elements = a & b
only_in_a = a - b
only_in_b = b - a
union_ab = a | b

print(common_elements)
print(only_in_a)
print(only_in_b)
print(union_ab)


# 11) INTEGRATION — LISTS ↔ SETS
# 11.1 From ["Michael Jackson","Thriller","Thriller",1982], create a structure
#       without duplicates and print it.

songs = ["Michael Jackson", "Thriller", "Thriller", 1982]
songs_unique = set(songs)
print(songs_unique)

# 11.2 Add "Bad" and print the structure.

songs_unique.add("Bad")
print(songs_unique)

# 11.3 Remove "Bad", then check if "Thriller" is present and print the boolean.

songs_unique.remove("Bad")
print("Thriller" in songs_unique)


# 12) INTEGRATION — LISTS ↔ TUPLES
# 12.1 With the tuple (5, 2, 8, 2, 10, 6), create a mutable structure with the same values,
#       change the first 2 to 20, then convert it back to an immutable structure and print it.

numbers_tuple = (5, 2, 8, 2, 10, 6)
numbers_list = list(numbers_tuple)

for idx, value in enumerate(numbers_list):
    if value == 2:
        numbers_list[idx] = 20
        break

numbers_tuple_final = tuple(numbers_list)
print(numbers_tuple_final)

# 12.2 Print how many times 2 appears in the final immutable structure
#      and the index of its first appearance (if it exists).

count_2 = numbers_tuple_final.count(2)
print(count_2)

if count_2 > 0:
    print(numbers_tuple_final.index(2))
else:
    print("2 does not appear in the final tuple.")


# 13) INTEGRATION — DICTIONARIES AND LISTS
# 13.1 Create a dictionary with name keys and birth year values for three people.
#      Print:
#      an alphabetically sorted list of names,
#      all values,
#      and the key–value pair for the youngest person.

birth_years = {
    "Alice": 1995,
    "Bob": 1990,
    "Charlie": 2001
}

sorted_names = sorted(birth_years.keys())
print(sorted_names)

print(list(birth_years.values()))

youngest_name = max(birth_years, key=birth_years.get)
print(youngest_name, birth_years[youngest_name])

# 13.2 Add a new person and print the full dictionary.

birth_years["Dani"] = 2002
print(birth_years)


# 14) INTEGRATION — DICTIONARIES AND SETS
# 14.1 Create:
#       d1 = {"a":1, "b":2, "c":3}
#       d2 = {"b":5, "c":6, "d":7}
#      Print:
#       common keys,
#       keys only in d1,
#       and the union of keys.

d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"b": 5, "c": 6, "d": 7}

keys1 = set(d1.keys())
keys2 = set(d2.keys())

common_keys = keys1 & keys2
only_in_d1 = keys1 - keys2
union_keys = keys1 | keys2

print(common_keys)
print(only_in_d1)
print(union_keys)

# 14.2 Build a new dictionary that:
#      keeps keys from d1 that are not in d2,
#      uses values from d2 for common keys,
#      and adds keys that exist only in d2.

merged_dict = {}

for key in d1:
    if key not in d2:
        merged_dict[key] = d1[key]

for key in d2:
    merged_dict[key] = d2[key]

print(merged_dict)


# 15) STRING → LIST → SET (CLEANING)
# 15.1 With the string "manzana, pera, manzana, kiwi, pera, mango",
#      create a list of words, then a structure without duplicates,
#      and then an alphabetically sorted structure of unique elements.

fruits_text = "manzana, pera, manzana, kiwi, pera, mango"
fruits_list = [word.strip() for word in fruits_text.split(",")]
print(fruits_list)

fruits_unique = set(fruits_list)
print(fruits_unique)

fruits_sorted_unique = sorted(fruits_unique)
print(fruits_sorted_unique)


# 16) MINI PROJECT — SIMPLE CONTACT BOOK
# 16.1 Create a structure to store people:
#       name (key),
#       data: another structure with "age" and "city".
#       Add at least 3 people.

contacts = {
    "Alice": {"age": 25, "city": "Madrid"},
    "Bob": {"age": 30, "city": "Barcelona"},
    "Charlie": {"age": 22, "city": "Valencia"}
}

# 16.2 Print names in alphabetical order.

for name in sorted(contacts.keys()):
    print(name)

# 16.3 Print all cities without duplicates in a suitable structure.

cities = {data["city"] for data in contacts.values()}
print(cities)

# 16.4 Remove one person by name and print the result.

contacts.pop("Alice")
print(contacts)

# 16.5 Change the city of one person and print the updated record.

contacts["Charlie"]["city"] = "Seville"
print("Charlie:", contacts["Charlie"])


# 17) MINI PROJECT — MUSIC LIBRARY
# 17.1 Create a list of albums. Each album must have:
#       "title", "artist", "year", "genres" (no duplicates).
#       Add at least 5 albums.

albums = [
    {
        "title": "Thriller",
        "artist": "Michael Jackson",
        "year": 1982,
        "genres": {"pop", "rock"}
    },
    {
        "title": "Back in Black",
        "artist": "AC/DC",
        "year": 1980,
        "genres": {"rock", "hard rock"}
    },
    {
        "title": "The Dark Side of the Moon",
        "artist": "Pink Floyd",
        "year": 1973,
        "genres": {"progressive rock"}
    },
    {
        "title": "Rumours",
        "artist": "Fleetwood Mac",
        "year": 1977,
        "genres": {"rock"}
    },
    {
        "title": "Random Access Memories",
        "artist": "Daft Punk",
        "year": 2013,
        "genres": {"electronic"}
    }
]

# 17.2 Print all titles in alphabetical order.

titles_sorted = sorted(album["title"] for album in albums)
print(titles_sorted)

# 17.3 Print all artists without duplicates.

artists = {album["artist"] for album in albums}
print(artists)

# 17.4 Print all albums published from a given year (for example, from 2000).

year_threshold = 2000
recent_albums = [album for album in albums if album["year"] >= year_threshold]
print(recent_albums)

# 17.5 Add a new genre to a specific album, avoiding duplicates.

for album in albums:
    if album["title"] == "Thriller":
        album["genres"].add("funk")

print([a for a in albums if a["title"] == "Thriller"])

# 17.6 Remove an album by title and print the resulting catalog.

title_to_remove = "Rumours"
albums = [album for album in albums if album["title"] != title_to_remove]
print(albums)









