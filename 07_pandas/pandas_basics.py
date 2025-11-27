import pandas as pd  # import pandas and name it as pd
# pd = pandas

"""
read_csv()
.head() -> shows the first 5 rows by default (you can specify how many)
.tail() -> shows the last 5 rows by default (you can specify how many)
Series()
DataFrame()
.values
"""

csv_path = "file.csv"  # store the CSV file path in a variable

df = pd.read_csv(csv_path)  # read CSV and store it in df

df.head()  # show the first five rows


# Reading an Excel file (.xlsx) is similar

xlsx_path = "file1.xlsx"
df = pd.read_excel(xlsx_path)  # read an Excel file


# A DataFrame in Pandas is a table-like data structure (similar to Excel or SQL)
# It is a table with rows and columns


# Convert a dictionary into a DataFrame using DataFrame()

songs = {
    'Album': ['Thriller', 'Back in Black', 'The Dark Side of the Moon',
              'The Bodyguard', 'Bat Out of Hell'],
    'Released': [1982, 1980, 1973, 1992, 1977],
    'Length': ['00:42:19', '00:42:11', '00:42:49', '00:57:44', '00:46:33']
}

df = pd.DataFrame(songs)  # convert the dictionary into a DataFrame

x = df[['Length']]  # select the Length column
print(x)

x = df[['Length', 'Released']]  # select multiple columns

"""
| Syntax            | Object Type | Description                       |
| ----------------- | ----------- | --------------------------------- |
| df['Length']      | Series      | Single column (1D)                |
| df[['Length']]    | DataFrame   | Subtable (2D) with one or more columns |
"""


# iloc (index location)
# df.iloc[row, column]

df.iloc[0, 0]  # example value


# Copy the DataFrame and change numeric indices to letters

df_new = df  # create a copy
df_new.index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']  # change index to letters


# loc (location by label)
# df.loc[index, column]

df.loc['a', 'Album']
df.loc['b', 'Album']


# Meaning of 0:2 and 0:3
# These are ranges (slices). The start is included, the end is excluded in iloc.

z = df.iloc[0:2, 0:3]
# 0:2 → rows 0 and 1
# 0:3 → columns 0, 1, 2

# loc includes the final label
z = df.loc[0:2, "Album":"Released"]


# unique() returns unique values in a column
df["Released"].unique()


# Boolean filtering
df["Released"] > 1979  # returns True/False for each row


# Create a new DataFrame with a condition
df1 = df[df["Released"] > 1979]


# Export to CSV
df1.to_csv("new_songs.csv")


# INTRODUCTION TO PANDAS

# Pandas = Python library for analysing and manipulating data (tables, lists, CSV files, etc.)

import pandas as pd

# SERIES
# A Series = single column (1D)

data = [10, 20, 30, 40, 50]
s = pd.Series(data)
print(s)

# Access elements
print(s[2])
print(s.iloc[3])
print(s[1:4])

# Common methods
s.values
s.index
s.mean()
s.unique()
s.isnull()


# DATAFRAME
# A DataFrame = table (2D)

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 28],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)
print(df)

# Select columns and rows
df['Name']
df[['Name', 'Age']]
df.iloc[2]
df.loc[1]

# Filtering
df1 = df[df['Age'] > 25]

# Unique values
df['City'].unique()


# METHODS AND ATTRIBUTES
df.shape
df.info()
df.describe()
df.head()
df.tail()
df.mean()
df.sort_values('Age')
df.groupby('City').mean()
df.fillna(0)
df.drop('City', axis=1)
df.rename(columns={'Name': 'Nombre'})


# IMPORT / EXPORT DATA
df = pd.read_csv('file.csv')
df.to_csv('new_file.csv')


# CONCLUSION
# Series → one column (1D)
# DataFrame → full table (2D)
# Pandas is essential for data cleaning, analysis and exporting.









