import requests
import numpy as np
import pandas as pd

# FULL PATH - GUIDED EXERCISES + NO-HELP EXERCISES
# ORDERED FROM EASIEST TO HARDEST


# BLOCK 1 – REQUESTS + JSON (BASICS)
# Based on: solicitudes_get_post_scraping.ipynb

# GUIDED SECTION

# 1) Make a GET request to a simple URL.
r = requests.get("https://picsum.photos/v2/list")
r

# 2) Show the status code.
r.status_code

# 3) Show only the first 300 characters of the response content.
r.text[0:300]

# 4) Store the response headers in a variable.
my_headers = r.headers
my_headers

# 5) Print only the value of "Content-Type".
my_headers["Content-Type"]

# 6) Make a GET request with parameters (example: name and city).
params = {"name": "Dani", "City": "Barcelona"}
r = requests.get("https://picsum.photos/v2/list", params=params)
r.url
r.json()
r.text

# 7) Make a request to an endpoint that returns JSON.
r = requests.get("https://api.adviceslip.com/advice")
r.text
r.url
r.json()
type(r.text)

# 8) Access a specific key inside the JSON (example: "args").
r = requests.get("https://httpbin.org/get", params={"name": "Dani", "city": "Barcelona"})

# 9) Explanation in comments:
# What is JSON?
# JSON stands for "JavaScript Object Notation".
# It is a text format used by APIs to send and receive data.
# It looks similar to a Python dictionary with "key": "value" pairs.
# Example: {"name": "Dani", "age": 23}

# Difference between r.text and r.json():
# - r.text returns the response as raw text (string).
# - r.json() converts that JSON text into a Python dictionary/list.

# When to use each one:
# - Use r.text when you want to see the content exactly as the server sends it
#   (HTML, plain text, debugging).
# - Use r.json() when you know the server returns JSON
#   and you want easy access to the data (for example data["name"]).

# 10) Make a request to a fake or broken URL.
try:
    r = requests.get("https://paginaquenoexiste123456.com")
    print(r.status_code)
except requests.exceptions.RequestException as e:
    print("Error making the request:", e)


# NO-HELP SECTION

# 1) Make a GET request to a URL and show:
#    - status code
#    - first 200 characters
#    - Content-Type

params = {"Nombre": "Luis", "Apellido": "Garcia"}
r = requests.get("https://dog.ceo/api/breeds/image/random", params=params)

r.status_code
r.text[:200]
r.headers["content-type"]

# 2) Make a GET with parameters (name, age, city) and show
#    exactly where those parameters appear in the JSON.

r = requests.get(
    "https://picsum.photos/v2/list",
    params={"name": "Dani", "age": 24, "city": "Barcelona"}
)

# 3) Convert a JSON response into a list and display 2 internal keys.
data = r.json()
data[0]
data[1]


# MINI CHALLENGE BLOCK 1
# Create a function that:
# - receives a URL
# - makes a request
# - returns:
#   * status code
#   * Content-Type
#   * content length

def healthy_url(url):
    r = requests.get(url)
    status = r.status_code
    ctype = r.headers.get("Content-Type", "not found")
    content_length = r.headers.get("Content-Length", "not found")
    print(f"Content status: {status}")
    print(f"Content-Type: {ctype}")
    print(f"Content length: {content_length}")


# BLOCK 2 – FILES WITH WITH OPEN (TEXT)
# Based on: withopen.ipynb

# GUIDED SECTION

# 1) Create a file "notas.txt" and write 3 lines of text.
with open("notas.txt", "w", encoding="utf-8") as f:
    f.write("First line\n")
    f.write("Second line\n")
    f.write("Third line\n")

# 2) Open "notas.txt" in read mode and display its full content.
with open("notas.txt", "r", encoding="UTF-8") as f:
    read = f.read()
print(read)

# 3) Open "notas.txt" again and iterate through it line by line.
with open("notas.txt", "r", encoding="UTF-8") as f:
    for line in f:
        print(line)

# 4) Create a list containing only the non-empty lines.
valid_lines = []
with open("notas.txt", "r", encoding="UTF-8") as f:
    for line in f:
        if line.strip() != "":
            valid_lines.append(line.strip())
print(valid_lines)

# 5) Open "notas.txt" in append mode and add a line at the end.
with open("notas.txt", "a", encoding="UTF-8") as f:
    f.write("i am fine thank you\n")

with open("notas.txt", "r", encoding="UTF-8") as f:
    read = f.read()
print(read)

# 6) Create a file "origen.txt" and then "copia.txt".
with open("origen.txt", "w", encoding="UTF-8") as f:
    f.write("my first friend\n")
    f.write("my second friend\n")
    f.write("my only friend\n")

with open("origen.txt", "r", encoding="UTF-8") as f1:
    with open("copia.txt", "w", encoding="UTF-8") as f2:
        for line in f1:
            f2.write(line)

print("Copy completed successfully")

# 7) Merge "notas.txt" and "origen.txt" into "fusion.txt".
with open("notas.txt", "r", encoding="UTF-8") as notas, \
     open("origen.txt", "r", encoding="UTF-8") as origen, \
     open("fusion.txt", "w", encoding="UTF-8") as fusion:
    fusion.write(notas.read())
    fusion.write("\n----------------------------------------\n")
    fusion.write(origen.read())


# NO-HELP SECTION

# 1) Create a file, write several lines, reopen it and display them.
with open("create.txt", "w", encoding="UTF-8") as c:
    c.write("Hello everybody\n")
    c.write("Hello everyone\n")

with open("create.txt", "r", encoding="UTF-8") as c:
    read = c.read()
read

# 2) Create an exact copy of that file with another name.
with open("create.txt", "r", encoding="UTF-8") as c, \
     open("newcopy.txt", "w", encoding="UTF-8") as new:
    for i in c:
        new.write(i)

# 3) Create a file that joins the content of two different files.
with open("create.txt", "r", encoding="UTF-8") as a, \
     open("newcopy.txt", "r", encoding="UTF-8") as b, \
     open("newnew.txt", "w", encoding="UTF-8") as c:
    c.write(a.read())
    c.write("\n................................\n")
    c.write(b.read())

# 4) Create a list with the lines that contain a specific word.
with open("newnew.txt", "r", encoding="UTF-8") as newnew, \
     open("newhello.txt", "w", encoding="UTF-8") as hello:
    for i in newnew:
        if "Hello" in i or "hello" in i:
            hello.write(i)

# 5) Write a summary into a new file with:
#    - number of lines of another file
#    - total number of characters.
with open("newhello.txt", "r", encoding="UTF-8") as newhello, \
     open("nexthello.txt", "w", encoding="UTF-8") as nextf:
    caract = 0
    lines = 0
    for line in newhello:
        caract += len(line)
        lines += 1
        nextf.write(line)
    nextf.write(str(caract) + "\n")
    nextf.write(str(lines) + "\n")


# MINI CHALLENGE BLOCK 2
# Mini note system:
# - a file where each line is a note
# - add a note
# - list notes
# - count notes

my_document = input("Add your file: ")
things = ""

while True:
    print("\nWelcome to the Note System")
    print("What do you want to do? select 1 - 4")
    print("1- Add new note")
    print("2- View all notes")
    print("3- Count how many notes there are")
    print("4- Exit")
    my_number = input("Choose an option (1-2-3-4): ")

    if my_number == "1":
        things = input("Which note do you want to add? ")
        with open(my_document, "a", encoding="UTF-8") as add:
            add.write(things + "\n")
        print(f"'{things}' added successfully.")
    elif my_number == "2":
        print("\nYOUR NOTES")
        with open(my_document, "r", encoding="UTF-8") as f:
            for line in f:
                print(line.strip())
    elif my_number == "3":
        counts = 0
        with open(my_document, "r", encoding="UTF-8") as f:
            for _ in f:
                counts += 1
        print(f"\nThere are {counts} notes.")
    elif my_number == "4":
        print("Exiting app, goodbye.")
        break
    else:
        print("Invalid option, try again.")


# BLOCK 3 – NUMPY 1D (NUMERIC BASICS)
# Based on: numpy.ipynb

# GUIDED SECTION

# 1) Create an array with numbers from 1 to 10.
n_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# 2) Print type, dtype, shape, size, ndim.
type(n_array)
n_array.dtype
n_array.shape
n_array.size
n_array.ndim

# 3) Change the first element to 99.
n_array[0] = 99

# 4) Change the last 3 elements to 0 using slicing.
n_array[-3:] = 0

# 5) Create another array from 10 to 1, add them and observe the result.
n2_array = np.arange(10, 0, -1)
n3_array = np.arange(1, 11)
f_array = n2_array + n3_array
f_array

# The sum is element-wise because NumPy applies vectorized operations:
# each position of one array sums with the same position of the other.

# 6) Calculate total sum, mean, max, min.
f_array.sum()
f_array.mean()
f_array.max()
f_array.min()


# NO-HELP SECTION

# 1) Create an array from 0 to 100 and calculate mean, sum, max, min.
wow_array = np.arange(0, 101, 1)
wow_array.mean()
wow_array.sum()
wow_array.max()
wow_array.min()

# 2) Create an array and set all values greater than 50 to 0.
wow_array = np.arange(0, 101, 1)
wow_array[wow_array > 50] = 0

# 3) Create two arrays of the same size and compute element-wise sum and product.
m1 = np.array([29, 1, 56, 2, 11, 45, 4, 76])
m2 = np.array([31, 22, 48, 9, 34, 66, 2, 81])
m3 = m1 + m2
m4 = m1 * m2


# MINI CHALLENGE BLOCK 3

students_notes = np.array([3, 7, 5, 6, 2, 1, 9, 6, 7, 7, 5, 5, 5, 6, 7, 9, 9, 6, 8, 6])

# count how many passed
passed = np.sum(students_notes >= 5)

# how many failed
failed = np.sum(students_notes < 5)

# average note
average_note = students_notes.mean()

# maximum note
max_note = np.max(students_notes)


# BLOCK 4 – NUMPY 2D (MATRICES)
# Based on: two_dimensional_numpy.ipynb

# GUIDED SECTION

# 1) Create a 2x3 matrix with numbers from 1 to 6.
n2 = np.arange(1, 7).reshape(2, 3)

# 2) Show shape, ndim, and type.
n2.shape
n2.ndim
type(n2)

# 3) Access element row 0, column 2.
n2[0, 2]

# 4) Get the entire first row.
n2[0]

# 5) Get the entire first column.
n2[:, 0]

# 6) Transpose the matrix.
n2.T

# 7) Create an array of 12 numbers and reshape to 3x4.
num_school = np.arange(1, 13)
num_school = num_school.reshape(3, 4)


# NO-HELP SECTION

# 1) Create a 3x3 matrix with values from 1 to 9.
array3x3 = np.arange(1, 10).reshape(3, 3)

# 2) Get the main diagonal.
diag = array3x3.diagonal()

# 3) Sum by rows.
sum_rows = array3x3.sum(axis=1)

# 4) Sum by columns.
sum_cols = array3x3.sum(axis=0)

# 5) Transpose the matrix and comment if something important changes.
array3x3.T
# The transpose swaps rows and columns.


# MINI CHALLENGE BLOCK 4
# 7x24 temperature table (7 days, 24 hours).
temperaturas = np.random.randint(10, 35, size=(7, 24))

# mean per day
temperaturas.mean(axis=1)

# mean per hour (column)
temperaturas.mean(axis=0)

# find max temperature and its position
max_temp = temperaturas.max()
indice_plano = temperaturas.argmax()
dia_max, hora_max = np.unravel_index(indice_plano, temperaturas.shape)


# BLOCK 5 – BASIC PANDAS
# Based on: pandas.ipynb

# GUIDED SECTION

# 1) Create a dictionary with lists: "Name", "Age", "City".
persons = {
    "Name": ["Dani", "Olga", "Jaime", "Sandra", "Ivan", "Lucia"],
    "Age": [24, 26, 21, 31, 33, 25],
    "City": ["Barcelona", "Londres", "Berlin", "Dublin", "Madrid", "Miami"]
}

psn = pd.DataFrame(persons)
print(persons)

# 2) Show first 3 rows and last 2 rows.
psn[:3]
psn[-2:]

# 3) Use iloc.
psn.iloc[0]
psn.iloc[2:5]
psn.iloc[:, 1]

# 4) Use loc to select columns.
psn.loc[:, ["Name", "Age"]]

# 5) Filter for Age > 25.
psn[psn["Age"] > 25]

# 6) Get unique values of "City".
psn["City"].unique()

# 7) Sort DataFrame by Age descending.
psn.sort_values("Age", ascending=False)

# 8) Save the DataFrame to a CSV file.
psn.to_csv("people.csv", index=False)

# 9) Load the CSV into a new DataFrame.
new = pd.read_csv("people.csv")


# NO-HELP SECTION

# 1) Create a DataFrame of students (name, note, group).
student = {
    "Name": ["Alex", "Ivan", "Miquel", "Liam", "Laura"],
    "Note": [7, 5, 6, 5, 4],
    "Group": ["A", "B", "A", "C", "D"]
}
st = pd.DataFrame(student)

# 2) Filter students with note >= 5.
st[st["Note"] >= 5]

# 3) Count how many students there are per group.
st.groupby("Group").size()

# 4) Sort by note descending.
st.sort_values("Note", ascending=False)

# 5) Save the result to a CSV (optional).
st.to_csv("students.csv", index=False)


# MINI CHALLENGE BLOCK 5
# DataFrame of products (name, category, price, stock).
productos = {
    "nombre": ["Teclado", "Camiseta", "Gorra", "Ratón", "Pantalón", "Monitor", "Mochila"],
    "categoria": ["Electrónica", "Ropa", "Accesorios", "Electrónica", "Ropa", "Electrónica", "Accesorios"],
    "precio": [25.99, 12.50, 8.99, 17.49, 29.99, 199.99, 45.00],
    "stock": [12, 40, 0, 30, 15, 0, 50]
}

pr = pd.DataFrame(productos)
pr

# products without stock
pr[pr["stock"] <= 0]

# expensive products (above the mean)
precio_medio = pr["precio"].mean()
pr[pr["precio"] > precio_medio]

# top 3 most expensive
pr.nlargest(3, "precio")

# how many products per category
pr.groupby("categoria")["nombre"].count()
