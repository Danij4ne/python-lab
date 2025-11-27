

# WORKING WITH DATA IN PYTHON — CHEAT SHEET


# READING AND WRITING FILES


# File opening modes
# r = read | w = write | a = append | + = update | b = binary
with open("data.txt", "r") as file:
    content = file.read()
    print(content)

with open("output.txt", "w") as file:
    file.write("Hello, world!")

with open("log.txt", "a") as file:
    file.write("Log entry: Something happened.")

with open("data.txt", "r+") as file:
    content = file.read()
    file.write("Updated content: " + content)


# File reading methods
with open("data.txt", "r") as file:
    lines = file.readlines()    # list of all lines
    next_line = file.readline() # reads next line
    content = file.read()       # reads entire file


# File writing methods
lines = ["Hello\n", "World\n"]
with open("output.txt", "w") as file:
    file.writelines(lines)


# Iterating over lines
with open("data.txt", "r") as file:
    for line in file:
        print(line)


# open() and close()
file = open("data.txt", "r")
content = file.read()
file.close()


# with open()
with open("data.txt", "r") as file:
    content = file.read()


# PANDAS

import pandas as pd

# Read CSV / Excel
df = pd.read_csv("data.csv")
df = pd.read_excel("data.xlsx")

# Write to CSV
df.to_csv("output.csv", index=False)

# Access columns
df["age"]
df[["name", "age"]]

# Describe statistics
df.describe()

# Drop columns or rows
df.drop(["age", "salary"], axis=1, inplace=True)   # drop columns
df.drop(index=[5, 10], axis=0, inplace=True)        # drop rows

# Drop NaN rows
df.dropna(axis=0, inplace=True)

# Find duplicated rows
duplicate_rows = df[df.duplicated()]

# Filter rows (conditional)
filtered_df = df[(df["age"] > 30) & (df["salary"] < 50000)]

# Group by
grouped = df.groupby(["category", "region"]).agg({"sales": "sum"})

# Head / Tail
df.head(5)
df.tail(5)

# Info summary
df.info()

# Merge DataFrames
# merged_df = pd.merge(df1, df2, on=["column1", "column2"])

# Replace values
df["status"].replace("In Progress", "Active", inplace=True)

# Print DataFrame
print(df)
df  # Jupyter auto-display


# NUMPY

import numpy as np

# Create arrays
array_1d = np.array([1, 2, 3])               # 1D array
array_2d = np.array([[1, 2], [3, 4]])        # 2D array
array_3d = np.array([[[1, 2], [3, 4]]])      # 3D array

# Array attributes
np.mean(array_1d)       # Mean value
np.sum(array_1d)        # Sum of all elements
np.min(array_1d)        # Minimum
np.max(array_1d)        # Maximum
np.dot(array_1d, array_1d)  # Dot product

# Math functions
np.sqrt(array_1d)       # Square root
np.exp(array_1d)        # Exponential
np.log(array_1d)        # Natural log

# Shape and transpose
array_2d.shape          # (rows, columns)
array_2d.reshape(1, 4)  # reshape into new shape
array_2d.T              # transpose

# Element-wise operations
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

a + b   # [5 7 9]
a - b   # [-3 -3 -3]
a * b   # [4 10 18]
a / b   # [0.25 0.4 0.5]
a @ b   # Dot product = 32


# END OF CHEAT SHEET
