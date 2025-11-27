# Sets
# Unlike other structures, sets are NOT ordered, which means they do not store element positions.
# Sets only contain unique elements.

my_set = {"Dani", "rock", "Pokemon", "Vampire", "rock", "chocolate"}
#                 duplicate                  duplicate

print(my_set)  # only one "rock" will remain because sets do not allow duplicates


# Casting → converting a list into a set

album_list = ["Michael Jackson", "Thriller", "Thriller", 1982]

album_set = set(album_list)  # convert album_list into a set to remove duplicates

print(album_set)

album_set.add("cake")  # add a new element

print(album_set)

album_set.remove("cake")  # remove an element

print("Dani" in album_set)  # True → the element is inside the set


# The issubset() method checks if one set is contained inside another.
# Returns True if all elements of the first set are inside the second one.

set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5}

print(set_a.issubset(set_b))  # True → all elements of 'a' are in 'b'
print(set_b.issubset(set_a))  # False → 'b' has more elements


# Main set methods in Python:

a = {1, 2, 3}
b = {3, 4, 5}

# union() → merge elements from both sets (no duplicates)
print(a.union(b))  # {1, 2, 3, 4, 5}

# intersection() → elements present in both sets
print(a.intersection(b))  # {3}

# difference() → elements in 'a' but not in 'b'
print(a.difference(b))  # {1, 2}

# b.difference(a) → elements in 'b' but not in 'a'
print(b.difference(a))  # {4, 5}


# Set example
fruits = {"apple", "banana", "orange"}
colors = {"red", "green", "blue", "orange"}

# discard() → removes an element, and if it does NOT exist, it does NOT raise an error
fruits.discard("apple")
fruits.discard("pear")   # nothing happens, no error
print(fruits)            # {'banana', 'orange'}

# issubset() → checks if a set is inside another
print(fruits.issubset(colors))  # False

# issuperset() → checks if a set contains another
print(colors.issuperset(fruits))  # False


# update() → add multiple elements at once to a set
fruits = {"apple", "banana"}

fruits.update(["kiwi", "grape"])

print(fruits)  # {'apple', 'banana', 'kiwi', 'grape'}

















