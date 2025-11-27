
# FUNCTIONS

"""
len()  → counts all elements
sum()  → sums all elements
min()  → returns the smallest number
max()  → returns the largest number

---- 2 ways to sort a list ----

1 - sorted()  → sorts a list (function). Returns a new sorted list or tuple.
2 - .sort()   → sorts the list in place. Does NOT return a new list.
"""


# Create our own functions

def add1(a):
    b = a + 1      # add 1 to 'a' and store it in a new variable
    return b       # return the value so it can be used outside

c = add1(5)        # assigns the result of add1(5) to variable c
print(c)           # c = 6


# Another function that multiplies two values

def mult(a, b):
    c = a * b
    return c

my_mult_result = mult(10, 2.33)
print(my_mult_result)


# Multiplying a number with a string

Jackson = mult(2, "Michael")
print(Jackson)  # repeats the string "Michael" two times


# Function without return

def mj():
    print("Michael Jackson")

mj()  # simply prints "Michael Jackson" when called


# pass → placeholder for an empty function body

def NoWork():
    pass  # Python doesn't allow an empty function body, so 'pass' is used

print(NoWork())  # prints None because the function has no return value


# Another example of add1 with printed explanation

def add1(a):
    b = a + 1
    print(a, "plus 1 equals", b)
    return b


# Using loops inside functions

def printStuff(Stuff):
    for i, s in enumerate(Stuff):   # enumerate gives index and value
        print("Album", i, "rating is", s)

album_rating = [10, 0, 8.5, 9.5]
printStuff(album_rating)


# Variadic parameters (*args) → allows variable number of arguments

def ArtistNames(*names):
    for name in names:
        print(name)

ArtistNames("Dani", "Emely", "John")


# Scope / Global scope

def AddDC(x):
    x = x + "DC"     # concatenates "DC"
    print(x)
    return x

x = "AC"
z = AddDC(x)         # prints "ACDC"


# Local variable inside a function

def Thriller():
    Date = 1982       # only exists inside the function
    return Date

print(Thriller())


# Make a variable inside a function global

def PinkFloyd():
    global ClaimedSales  # makes the variable global
    ClaimedSales = "45 million"
    return ClaimedSales

print(PinkFloyd())
print(ClaimedSales)   # also accessible outside the function


# Print numbers from 1 to a limit

def print_numbers(limit):
    for i in range(1, limit + 1):
        print(i)

print_numbers(5)  # Output: 1 2 3 4 5


# Function to add elements to a list

my_list = []

def add_element(data_structure, element):
    data_structure.append(element)

add_element(my_list, 42)
print(my_list)


# Function to remove elements from a list

def remove_element(data_structure, element):
    if element in data_structure:
        data_structure.remove(element)
    else:
        print(f"{element} not found in the list.")

remove_element(my_list, 17)




 









