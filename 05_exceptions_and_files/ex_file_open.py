
# PRACTICE: FILE HANDLING IN PYTHON — EXERCISE SHEET
# Rules:
# - No solutions were originally provided (this file now contains one possible solution).
# - Write and test everything step by step.

# A) Warm-up: open and modes  (WITH HINT)
 
# 1) File mode and name.
# Open "resources/data/Example2.txt" in read mode and show .mode and .name. Then close the file.
# HINT: open(..., "r"); use .mode and .name; close() at the end.
# Your code here:

with open("resources/data/Example2.txt", "r") as data_example:
    print("Open mode: ", data_example.mode)
    print("File name:", data_example.name)


# 2) Basic with open.
# Read all the content of "Example1.txt" using with open. Show if the file is closed inside
# and outside the with block.
# HINT: print(file.closed) inside and outside the block.
# Your code here:

with open("Example1.txt", "r") as my_file:
    content = my_file.read()
    print("Inside with, file.closed:", my_file.closed)

print("Outside with, file.closed:", my_file.closed)
print("File content:")
print(content)


# 3) Partial reading with readline(n).
# Read the first line completely and then only 4 characters from the second line. Show both.
# HINT: call readline() and then readline(4).
# Your code here:

with open("file.txt", "r") as my_file:
    first_line = my_file.readline()
    second_part = my_file.readline(4)

print("First line:", first_line.rstrip("\n"))
print("First 4 characters of second line:", second_part)


# 4) Mode differences.
# Open "temp_demo.txt" with "w", write one line; open again with "a", add another line;
# read with "r" to verify the result.
# HINT: "w" overwrites; "a" appends.
# Your code here:

with open("temp_demo.txt", "w", encoding="utf-8") as my_file:
    my_file.write("First line written in write mode.\n")

with open("temp_demo.txt", "a", encoding="utf-8") as my_file:
    my_file.write("Second line added in append mode.\n")

with open("temp_demo.txt", "r", encoding="utf-8") as my_file:
    print("Content of temp_demo.txt:")
    print(my_file.read())


# 5) rb and wb (binary).
# Create "demo.bin": write some bytes and then read them back to verify.
# HINT: open(..., "wb"), b"..."; then open(..., "rb").
# Your code here:

with open("demo.bin", "wb") as bin_file:
    bin_file.write(b"Hello friend")

with open("demo.bin", "rb") as bin_file:
    data = bin_file.read()
    print("Binary content read from demo.bin:", data)


 
# B) Reading in loops and cleaning lines  (WITH HINT)
 

# 6) Infinite loop with readline.
# Iterate over "file.txt" using while True + readline(); stop at the end; print each line without the newline.
# HINT: if not line: break; use .strip().
# Your code here:

with open("file.txt", "r", encoding="utf-8") as my_file:
    while True:
        line = my_file.readline()
        if not line:
            break
        print(line.strip())


# 7) for line in file loop.
# Iterate over "text.txt" and print: "Iteration i: <line>" with a counter starting at 0.
# HINT: i = 0; i += 1 in each loop.
# Your code here:

with open("text.txt", "r", encoding="utf-8") as my_file:
    i = 0
    for line in my_file:
        print(f"Iteration {i}: {line.strip()}")
        i += 1


# 8) Count non-empty lines.
# Count how many lines are not empty in "text.txt" and show the result.
# HINT: if line.strip(): count it.
# Your code here:

non_empty_lines = 0

with open("text.txt", "r", encoding="utf-8") as my_file:
    for line in my_file:
        if line.strip():
            non_empty_lines += 1

print("Non-empty lines in text.txt:", non_empty_lines)


# 9) Count total words.
# Count the total number of words in "text.txt".
# HINT: accumulate len(line.split()).
# Your code here:

total_words = 0

with open("text.txt", "r", encoding="utf-8") as my_file:
    for line in my_file:
        total_words += len(line.split())

print("Total words in text.txt:", total_words)


# 10) Filter by keyword.
# Print only the lines that contain the word "important" (case insensitive).
# HINT: "important" in line.lower().
# Your code here:

with open("text.txt", "r", encoding="utf-8") as my_file:
    print('Lines containing the word "important":')
    for line in my_file:
        if "important" in line.lower():
            print(line.strip())


# C) File pointer: tell and seek  (NO HINTS)
 

# 11) Initial position with a+.
# Open "file.txt" with "a+", show the initial position, try to read, go back to the start with seek
# and read everything. Show the position after reading.
# Your code here:

with open("file.txt", "a+", encoding="utf-8") as my_file:
    print("Initial position (a+):", my_file.tell())
    # Try to read from the end (normally returns empty string)
    content_from_end = my_file.read()
    print("Read from current position (likely empty):", repr(content_from_end))
    my_file.seek(0)
    full_content = my_file.read()
    print("Content after seek(0):")
    print(full_content)
    print("Final position:", my_file.tell())


# 12) seek from start, current and end.
# In "file.txt", move 5 bytes from the start, 3 from the current position and 0 from the end.
# Show tell() after each step. (Use binary mode for reliable byte offsets.)
# Your code here:

with open("file.txt", "rb") as my_file:
    print("Initial position:", my_file.tell())

    my_file.seek(5, 0)   # 5 bytes from the beginning
    print("Position after seek(5, 0):", my_file.tell())

    my_file.seek(3, 1)   # 3 bytes from current position
    print("Position after seek(3, 1):", my_file.tell())

    my_file.seek(0, 2)   # 0 bytes from the end
    print("Position after seek(0, 2):", my_file.tell())


# 13) Cut header using seek.
# Given a file with a known header length, move the pointer just after the header and read the rest.
# Your code here:

with open("data.txt", "r", encoding="utf-8") as file:
    header_length = 10  # known header length
    file.seek(header_length)
    rest_of_file = file.read()
    print("Content without header:")
    print(rest_of_file)


 
# D) Writing and modes (w, a, a+)
 

# 14) Write a list of lines.
# Create a list with several lines, write it to a new file and then verify its content by reading it.
# Your code here:

lines_to_write = [
    "First line in the list.\n",
    "Second line in the list.\n",
    "Third line in the list.\n",
]

with open("lista.txt", "w", encoding="utf-8") as my_list_file:
    my_list_file.writelines(lines_to_write)

with open("lista.txt", "r", encoding="utf-8") as my_list_file:
    print("Content of lista.txt:")
    print(my_list_file.read())

 
# E) Copy and merge files
 

# 18) Copy file line by line.
# Copy the content of one file into another, reading and writing line by line.
# Your code here:

with open("lista.txt", "r", encoding="utf-8") as source, open(
    "copia.txt", "w", encoding="utf-8"
) as target:
    for line in source:
        target.write(line)


# 19) Merge files with a separator.
# Merge two text files into a new one, adding a separator line between both contents.
# Your code here:

with open("lista.txt", "r", encoding="utf-8") as file1, open(
    "copia.txt", "r", encoding="utf-8"
) as file2, open("fusion.txt", "w", encoding="utf-8") as merged:
    for line in file1:
        merged.write(line)

    merged.write("\n--- SEPARATOR ---\n")

    for line in file2:
        merged.write(line)

with open("fusion.txt", "r", encoding="utf-8") as fusion_result:
    print("Content of fusion.txt:")
    print(fusion_result.read())


# 20) Temporary copy and replacement.
# Create a temporary copy of a file and then replace the original with that copy.
# (Here we just create a copy and verify it exists.)
# Your code here:

import shutil
import os

shutil.copy("fusion.txt", "copyfusion.txt")

if os.path.exists("copyfusion.txt"):
    print("The file was copied correctly.")
else:
    print("Copy file was not found.")


# 21) Merge avoiding duplicates.
# Merge two text files, but do not repeat lines that already exist in the first file.
# Your code here:

file1 = "copyfusion.txt"
file2 = "fusion.txt"
file3 = "newfusion.txt"

with open(file1, "r", encoding="utf-8") as f1:
    lines_file1 = set(f1.readlines())

with open(file2, "r", encoding="utf-8") as f2:
    lines_file2 = f2.readlines()
    for line in lines_file2:
        if line not in lines_file1:
            lines_file1.add(line)

with open(file3, "w", encoding="utf-8") as f3:
    # write lines in some stable order; here we sort them
    f3.writelines(sorted(lines_file1))


# F) Text formatting (.format / f-strings)
 

# 22) Report with .format.
# Show a message with file name, number of lines and size in bytes using .format().
# Your code here:

report_file = "newfusion.txt"

with open(report_file, "r", encoding="utf-8") as file:
    num_lines = sum(1 for _ in file)

size_bytes = os.path.getsize(report_file)

print(
    "File: {}, lines: {}, size: {}B".format(
        report_file, num_lines, size_bytes
    )
)


# 23) Report with f-strings.
# Repeat the previous exercise, but using f-strings.
# Your code here:

with open(report_file, "r", encoding="utf-8") as file:
    num_lines = sum(1 for _ in file)

size_bytes = os.path.getsize(report_file)

print(f"File: {report_file}, lines: {num_lines}, size: {size_bytes}B")


# 24) Aligned table.
# Create a table with two columns (Name, Value) and show the data aligned using fixed widths.
# Your code here:

name = report_file
lines = num_lines
size = size_bytes

print(f"{'Name':<12} {'Value':>10}")
print(f"{'File':<12} {name:>10}")
print(f"{'Lines':<12} {lines:>10}")
print(f"{'Size (B)':<12} {size:>10}")





