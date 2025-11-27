# FOR LOOP — RANGE

for i in range(10):  # prints numbers from 0 to 9
    print(i)

for i in range(5, 10):  # prints numbers from 5 to 9
    print(i)

for i in range(1, 10, 4):  # prints 1, 5, 9 (step of 4)
    print(i)


# Looping through a list
squares = ["red", "yellow", "green"]

for square in squares:  # iterates through each element in the list
    print(square)       # prints each one


# WHILE loop example
# While = similar to for, but it only runs while the condition is True

squares = ["orange", "orange", "purple", "orange", "blue"]

new_squares = []
i = 0

while squares[i] == "orange":  # continues while the element is "orange"
    new_squares.append(squares[i])
    i += 1

print(new_squares)


# enumerate(): adds an index to each element of a list
fruits = ["apple", "banana", "orange"]

for index, fruit in enumerate(fruits):  # index = position, fruit = value
    print(f"At position {index}, I found a {fruit}")


# WHILE TRUE → infinite loop until a break is used

i = 0
while True:  # infinite loop until break
    print("Iteration number:", i)
    i += 1

    if i == 3:  # exit condition
        print("End of loop with break")
        break


# WHILE NOT: runs while the condition is FALSE

x = 0

while not x == 3:  # repeats while x is NOT equal to 3
    print("x is:", x)
    x += 1

print("The loop ended because x == 3")


# Loop through a list of colors and print each color with its index using enumerate
color_list = ["red", "blue", "green", "yellow"]

for index, color in enumerate(color_list):
    print(color, index)


# Looping through indexes using range(len(...))
dates = [1982, 1980, 1973]
N = len(dates)

for i in range(N):  # generates indices 0, 1, 2
    print(dates[i])


# continue and break example
count = 0

while count < 10:
    count += 1

    if count == 3:
        continue  # skips the rest of this iteration (does NOT print 3)

    if count == 8:
        break  # fully exits the loop before printing 8

    print(count)
