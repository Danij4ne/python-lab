
# Level 1 — Beginner with Support

# Exercise 1 — Load and explore data
# 1) Import pandas and store the file "songs.csv" in a variable.
import pandas as pd

csv_file = "songs.csv"

# 2) Load the file with read_csv().
pd_songs = pd.read_csv(csv_file)
print(pd_songs)

# 3) Show the first 5 rows and the last 2 rows of the DataFrame.
pd_songs.head()
pd_songs.tail(2)


# Exercise 2 — View DataFrame structure

# 1) Show the size of the DataFrame (rows, columns).
pd_songs.shape

# 2) Show general information about the DataFrame (data types and nulls).
pd_songs.info()

# 3) Show basic statistics (mean, max, min, etc.) of numeric columns.
pd_songs.describe()


# Exercise 3 — Select columns and rows

# 1) Select only the "Album" column.
pd_songs["Album"]

# 2) Select the columns "Album" and "Released".
pd_songs[["Album", "Released"]]

# 3) Access the first row of the DataFrame.
pd_songs.iloc[0]

# 4) Access the second row using its label (loc).
pd_songs.loc[1]


# Exercise 4 — Filter data

# 1) Create a new DataFrame called df1 with songs released after 1979.
df1 = pd_songs[pd_songs["Released"] > 1979]

# 2) Show that new DataFrame.
print(df1)


# Exercise 5 — Useful methods

# 1) Show the unique values of the "Released" column.
pdr = pd_songs["Released"].unique()
print(pdr)

# 2) Save the new DataFrame df1 into a file called "new_songs.csv".
df1.to_csv("new_songs.csv", index=False)


# Exercise 6 — Series

# 1) Create a Series with the values [10, 20, 30, 40, 50].
serie = pd.Series([10, 20, 30, 40, 50])
print(serie)

# 2) Show the value at position 2.
print(serie[2])

# 3) Calculate the mean.
serie.mean()

# 4) Show the unique values.
serie.unique()


# Level 2 — Advanced without support

# Exercise 1 — Load and review

# Load the file "songs.csv".
file = pd.read_csv("songs.csv")

# Show the first 3 rows.
file.head(3)

# Show how many rows and columns the DataFrame has.
file.shape


# Exercise 2 — Access and selection

# Select the column "Artist".
pda = file[["Artist"]]

# Select rows 0, 1 and 2 and columns from "Artist" to "Released" (included).
nfile = file[["Artist", "Released"]]
nfile.iloc[[0, 1, 2]]

# Alternative:
file.loc[0:2, ["Artist", "Released"]]


# Exercise 3 — Filtering and export

# Create a new DataFrame with songs released between 1980 and 1990 (both included).
newfile = file[(file["Released"] >= 1980) & (file["Released"] <= 1990)]
newfile

# Save that new DataFrame into a file called "songs_80s.csv".
newfile.to_csv("songs_80s.csv")


# Exercise 4 — Basic analysis

# Show how many different release years exist.
file["Released"].unique()

# Calculate the average of the "Released" column.
file["Released"].median()


# Exercise 5 — Create your own DataFrame

# Create a DataFrame with your favourite songs
# (4 columns: Artist, Album, Released, Length).
my_new_songs = pd.DataFrame({
    "Artist": ("Maluma", "Shakira", "Enrique", "Alvaro"),
    "Album": ("Conster", "Goast", "Kasti", "Goal"),
    "Released": ("2013", "2005", "1998", "2020")
})

# Save it to a file called "my_songs.csv".
my_new_songs.to_csv("my_songs.csv")


# Exercise 6 — Expert level

# Create a copy of the main DataFrame.
copy_new_songs = my_new_songs.copy()

# Replace numeric indexes with letters (a, b, c...).
copy_new_songs.index = ["A", "B", "C", "D"]

# Access a value using loc[].
copy_new_songs.loc["A"]
