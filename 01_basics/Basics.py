# Check data types with type()

my_int = 5
print(type(my_int))

my_str = "Hello"
print(type(my_str))

my_float = 4.5
print(type(my_float))

my_bool = True
print(type(my_bool))

print(10 // 3)   # integer division (no decimals)
print(10 / 3)    # float division (with decimals)

x = 4
x = x / 2
print(x)         # division always returns float even if result is an integer


famous_name = "Michael Jackson"

print(famous_name[::2])   # steps of 2 (skips characters)
print(famous_name[:2])    # prints the first 2 characters
print(famous_name[2:])    # prints everything except the first 2
print(famous_name[2:5])   # prints positions 2 to 4 (5 not included)

famous_3_name = 3 * "Michael Jackson"   # repeats the string 3 times
print(famous_3_name)

#############

print("Michael Jackson \n is the best")   # \n = newline
print("Michael Jackson \t is the best")   # \t = tab (large space)
print("Michael Jackson \\ is the best")   # prints a backslash

# r" " creates a raw string (useful for file paths or regex)
print(r"Michael Jackson \ or \n is the best")

##############

# upper() → converts to UPPERCASE
name = "Juanjo Gutierrez".upper()
print(name)

# replace() → replaces one substring with another
name = "Juan Gonzalez"
new_name = name.replace("Juan", "Alvaro")
# replace() returns a NEW string; the original is not modified
print(new_name)

# find() → returns the index where a substring appears
my_thing = "pelota"
print(my_thing.find("lo"))   # result: 2 (because 'l' is at position 2)

"""
function(name)   -> global function

name.function()  -> method exclusive to the type (str, int, float, etc.)
"""

###############

# String formatting

name = "Dani"
age = 24

print(f"my name is {name} and my age is {age}")   # f-string formatting

# Formatting v2 (format method)
print("my name is {} and my age is {}".format(name, age))

# Formatting v3 (old % formatting)
print("my name is %s and my age is %d" % (name, age))

####################

# split() → splits a string into a list based on a separator
my_string = "Hello , my friend , my name is Dani"
split_text = my_string.split(",")   # splits on every comma
print(split_text)

# strip() → removes whitespace at the beginning and end
my_string = "Hello"
trimmed = my_string.strip()
print(trimmed)

# Common string methods: .split(), .lower(), .upper(), etc.

# Python escape sequences: \n, \t, \\, etc.

























































































