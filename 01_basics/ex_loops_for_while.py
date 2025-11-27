
# LEVEL 1 — FOR LOOP + RANGE

# 1. Print numbers from 0 to 5 using range().
for i in range(6):
    print(i)

# 2. Print only even numbers from 0 to 10 (using step=2).
for i in range(0, 12, 2):
    print(i)

# 3. Print numbers from 10 to 1 in descending order.
for i in range(10, 0, -1):
    print(i)

# 4. Use a for loop to sum numbers from 1 to 5 and print the total.
total = 0
for i in range(1, 6):
    total += i
print(total)


# LEVEL 2 — FOR with LISTS and ENUMERATE

# 5. Iterate over the list of colors and print each color with its index.
color_list = ["red", "blue", "green", "yellow"]

for index, color in enumerate(color_list):
    print(index, color)

# 6. Given a list ["apple", "banana", "cherry"], print "I like apple", etc.
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(f"I like {fruit}")


# LEVEL 3 — BASIC WHILE

# 7. Use a while loop to print numbers from 1 to 5.
i = 1
while i <= 5:
    print(i)
    i += 1

# 8. Use a while loop to print numbers less than 10 that are multiples of 3.
i = 0
while i <= 10:
    if i % 3 == 0:
        print(i)
    i += 1


# LEVEL 4 — WHILE TRUE + BREAK

# 9. Ask for a number repeatedly.
# If the user enters 0 → print "End of program" and break.
# Otherwise → print the number and continue.

while True:
    user_number = int(input("Enter a number: "))
    if user_number == 0:
        print("End of program.")
        break
    else:
        print(f"You entered {user_number}. Try again.")


# LEVEL 5 — WHILE NOT

# 10. Repeat the loop until the variable "key" equals "python".
key = ""

while key != "python":
    key = input("Enter the key: ")
    if key == "python":
        print("Correct!")


# LEVEL 6 — FINAL CHALLENGE

# 11. Use for + range to print a multiplication table (example: table of 3).
for i in range(1, 11):
    print(f"3 x {i} = {3 * i}")

# 12. Use a while loop to extract only "orange" elements from the list.
colors = ["orange", "green", "blue", "orange", "red"]
only_orange = []

i = 0
while i < len(colors):
    if colors[i] == "orange":
        only_orange.append(colors[i])
    i += 1

print(only_orange)  # ['orange', 'orange']




































