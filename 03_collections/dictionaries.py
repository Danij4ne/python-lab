# Dictionaries
# They contain keys and values. Values can be mutable or immutable, and can be duplicated.
# The key is used to access the value.

my_dictionary = {"Name": "Dani", "Nickname": "Danij"}
#                   key       value     key       value

print(my_dictionary["Name"])     # Using the key, we access the value

my_dictionary["Friend"] = "Antonio"   # Add a new key-value pair

print(my_dictionary)

del(my_dictionary["Friend"])     # Delete a specific key-value pair

print(my_dictionary)

print("Name" in my_dictionary)   # "in" checks if a key exists (returns True/False)

print(my_dictionary.keys())      # .keys() returns all keys

print(my_dictionary.values())    # .values() returns all values


#######################################

# Dictionary with different types of values
# "A": integer, "B": string, "C": list [], "D": tuple (), "E" and "F": integers
Dict = {"A": 1, "B": "2", "C": [3, 3, 3], "D": (4, 4, 4), "E": 5, "F": 6}


# update() – adds or updates key-value pairs in a dictionary
my_dictionary.update({"Profession": "Doctor"})
# dict_name.update({key: value})


# clear() – empties the dictionary
my_dictionary.clear()


# copy() – creates a shallow copy of the dictionary
my_new_dictionary = my_dictionary.copy()


# .items() – returns both keys and values together
person = {"name": "Dani", "age": 23}

print(person.items())
# Output: dict_items([('name', 'Dani'), ('age', 23)])
