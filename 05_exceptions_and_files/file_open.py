file1 = open("resources/data/Example2.txt", "r")  # r = read
# Path = resources/data/   file name = Example2.txt

file1.mode  # used to check the mode in which the file was opened, e.g. "r"

"""
File open modes in Python

"r"   → read only. Opens the file if it exists.
"w"   → write. Creates a new file or overwrites it if it already exists.
"a"   → append. Writes at the end of the file without removing existing content.

"rb"  → read binary. Used with images, audio, etc.
"wb"  → write binary. Creates or overwrites binary files.

"r+"  → read and write. Opens an existing file for both operations.
"w+"  → write and read. Creates or overwrites the file and allows reading.
"a+"  → append and read. Appends content to the end and also allows reading.

"x"   → exclusive creation. Creates a new file and raises an error if it already exists.
"xb"  → exclusive creation in binary mode.
"x+"  → exclusive creation with read/write. Error if the file already exists.
"""

file1 = open("resources/data/Example2.txt", "r")
print(file1.mode)   # prints 'r'
print(file1.name)   # prints the file path / name
file1.close()

# with open is better practice than open alone because with open closes the file automatically

with open("Example1.txt", "r") as file1:
    file_contents = file1.read()  # read() reads the whole file into a string
    print(file_contents)
    print(file1.closed)  # False inside the with block
    print(file_contents)

with open("Example1.txt", "r") as file1:
    file_line = file1.readline()     # reads one line from the file
    file_line = file1.readline(4)    # reads only 4 characters of the next line
    # readline() can be called multiple times to read line by line

# when the file is not in the same folder as your .py you must include the relative path
with open("resources/data/Example1.txt", "r") as file1:
    content = file1.read()

# with open + if

with open("example.txt", "r") as file:
    line1 = file.readline()  # first line
    line2 = file.readline()  # second line

    print(line1)

    if "important" in line2:
        print("This line is important!")

# with open + while loop

with open("example.txt", "r") as file:
    while True:
        line = file.readline()
        if not line:  # no more lines
            break
        print(line.strip())  # print line without trailing newline

# with open + for loop

with open("example.txt", "r") as file1:
    i = 0
    for line in file1:
        print("Iteration", str(i), ": ", line)
        i = i + 1

# file.seek()

with open("texto.txt", "r") as file:
    file.seek(5)          # move the pointer to byte position 5
    text = file.read()    # read from that position until the end
    print(text)


# Example of using requests to download a text file (alternative to pyfetch in browsers)
import requests
import pandas as pd  # commonly used later to read data files with read_csv/read_table

url = (
    "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/"
    "IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt"
)

# Example (commented) of a typical download with requests:
# response = requests.get(url)
# if response.status_code == 200:
#     with open("example1.txt", "wb") as f:
#         f.write(response.content)


# Writing files with with open

with open("resources/data/Example2.txt", "w") as file1:
    file1.write("This is line A\n")
    file1.write("This is line B\n")

# Copying a file line by line

with open("Example1.txt", "r") as readfile:
    with open("Example3.txt", "w") as writefile:
        for line in readfile:
            writefile.write(line)

# Same idea with more comments

with open("Example1.txt", "r") as readfile:  # open original file in read mode
    with open("Example3.txt", "w") as writefile:  # open or create target file in write mode
        # "w" overwrites existing content if the file already exists
        for line in readfile:
            # line contains one line from the original file on each iteration
            writefile.write(line)  # copy the line into the new file

# Writing multiple lines automatically with a loop

lines = ["This is line A\n", "This is line B\n", "This is line C\n"]

with open("/Example2.txt", "w") as writefile:
    for line in lines:
        print(line)
        writefile.write(line)

# "a+" → append and read
# append text at the end and also allows reading

with open("Example2.txt", "a+") as testwritefile:
    testwritefile.write("This is line E\n")
    testwritefile.seek(0)            # move pointer to the beginning
    print(testwritefile.read())      # read entire content

# file.tell() → returns the current position of the pointer in the file (in bytes)
# file.seek(offset, from_what) → moves the pointer
#   offset → how many bytes to move
#   from_what → reference point: 0 = start, 1 = current, 2 = end

with open("Example2.txt", "a+") as testwritefile:
    print("Initial Location: {}".format(testwritefile.tell()))

    data = testwritefile.read()

    if not data:
        print("Read nothing")
    else:
        print(data)

    testwritefile.seek(0, 0)
    print("\nNew Location : {}".format(testwritefile.tell()))

    data = testwritefile.read()

    if not data:
        print("Read nothing")
    else:
        print(data)

    print("Location after read: {}".format(testwritefile.tell()))

# Example of .format():
# x = 10
# y = 5
# print("x = {}, y = {}, sum = {}".format(x, y, x + y))


# ===============================================
# Utilities for CSV/TXT files with commas
# ===============================================
# Goal:
# 1) Detect if the file has any "no" in the Active column.
# 2) Move all rows with Active == "no" from currentMem.txt to exMem.txt
#    - Keep the header in both files.
#    - Preserve line format (read/write full lines).
# 3) Clear a file safely.
#
# Assumption: files are simple CSV comma-separated text
# and there is a column called "Active", for example:
# MemberNumber,Name,Active
# 1,John,yes

import os


def _read_lines(path: str):
    """Read all lines from the file (including newline characters)."""
    with open(path, "r", encoding="utf-8") as f:
        return f.readlines()


def _write_lines(path: str, lines, mode: str = "w"):
    """
    Write a list of lines to a file.

    mode="w" → overwrite
    mode="a" → append at the end
    """
    with open(path, mode, encoding="utf-8") as f:
        f.writelines(lines)


def _file_empty_or_missing(path: str) -> bool:
    """Return True if the file does not exist or its size is 0 bytes."""
    return (not os.path.exists(path)) or os.path.getsize(path) == 0


def has_inactive_in_active_column(current_path: str) -> bool:
    """
    Return True if there is at least one row with Active == 'no' (case-insensitive).
    Return False otherwise.
    """
    lines = _read_lines(current_path)
    if not lines:
        return False

    header = lines[0].rstrip("\n")
    cols = [c.strip() for c in header.split(",")]

    try:
        idx_active = [c.lower() for c in cols].index("active")
    except ValueError:
        # There is no Active column
        return False

    for line in lines[1:]:
        if not line.strip():
            continue
        cells = [c.strip() for c in line.rstrip("\n").split(",")]
        if len(cells) > idx_active and cells[idx_active].lower() == "no":
            return True

    return False


def move_inactive_from_current_to_ex(current_path: str, ex_path: str) -> None:
    """
    Read current_path, separate active (yes) and inactive (no) rows,
    rewrite current_path with only active rows, and append inactive
    rows to ex_path.

    Rules:
    - Preserve the header (first line) in both files.
    - Work with whole lines (we only parse columns to check Active).
    """
    lines = _read_lines(current_path)
    if not lines:
        return

    header = lines[0]
    cols = [c.strip() for c in header.rstrip("\n").split(",")]

    try:
        idx_active = [c.lower() for c in cols].index("active")
    except ValueError:
        # No Active column found, nothing is moved
        return

    active_lines = [header]
    inactive_lines = []

    for line in lines[1:]:
        if not line.strip():
            # optional: keep blank lines with active section
            active_lines.append(line)
            continue

        cells = [c.strip() for c in line.rstrip("\n").split(",")]
        if len(cells) > idx_active and cells[idx_active].lower() == "no":
            inactive_lines.append(line)
        else:
            active_lines.append(line)

    # 1) Rewrite current_path with active rows only
    _write_lines(current_path, active_lines, mode="w")

    # 2) Append inactive rows to ex_path, ensuring ex_path has a header
    if inactive_lines:
        if _file_empty_or_missing(ex_path):
            _write_lines(ex_path, [header], mode="w")
            _write_lines(ex_path, inactive_lines, mode="a")
        else:
            _write_lines(ex_path, inactive_lines, mode="a")


def clear_file(path: str) -> None:
    """
    Empty a file completely (leave it with size 0 bytes).
    Warning: this removes all content.
    """
    open(path, "w", encoding="utf-8").close()

# Example usage (commented):
# current = "currentMem.txt"
# ex = "exMem.txt"
#
# if has_inactive_in_active_column(current):
#     print("There are inactive members in the file.")
# else:
#     print("No inactive members found.")
#
# move_inactive_from_current_to_ex(current, ex)
# clear_file(ex)





































