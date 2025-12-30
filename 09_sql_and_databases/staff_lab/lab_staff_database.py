 
# LAB: Database Access with Python (SQLite + Pandas)
# File: lab_staff_database.py
 
# This file is divided into two parts:
#
#   1) THEORY   (step-by-step explanation of the entire lab)
#   2) PRACTICE (the code that actually runs)
#
 
# 1. THEORY - DATABASE ACCESS WITH PYTHON
 
# ---------------------
# 1.1. What is SQLite?
# ---------------------
# SQLite is a very lightweight database engine that stores all
# information in a single file with a .db extension.
#
# Important characteristics:
#   - It does not require a server (no "service" like MySQL or PostgreSQL).
#   - No extra installation needed; it comes included with Python.
#   - It is perfect for practicing SQL and Data Engineering locally.
#
# To connect to an SQLite database from Python:
#
#       import sqlite3
#       conn = sqlite3.connect("STAFF.db")
#
# If the file STAFF.db does not exist, SQLite creates it automatically.
# If it already exists, it simply connects to it.
#
# The variable conn is a "bridge" (connection) between your Python code
# and the database.
#
# Whenever you finish using the database, you must close the connection:
#
#       conn.close()
#
# --------------------------------------
# 1.2. What is pandas in this context?
# --------------------------------------
# Pandas is a Python library widely used to work with tabular data.
# Two very important things for this lab:
#
#   1) Read a CSV into a DataFrame:
#
#       import pandas as pd
#       df = pd.read_csv("INSTRUCTOR.csv")
#
#   2) Save a DataFrame as a database table:
#
#       df.to_sql("INSTRUCTOR", conn, if_exists="replace", index=False)
#
# Where:
#   - "INSTRUCTOR" is the name of the table created in the database.
#   - conn is the connection created with sqlite3.connect().
#   - if_exists:
#       * 'fail'    -> raises an error if the table already exists.
#       * 'replace' -> deletes the existing table and creates a new one.
#       * 'append'  -> adds rows to the existing table.
#   - index=False -> indicates NOT to store the DataFrame index
#                    as an additional column in the table.
#
# Additionally, pandas allows executing SQL queries and returning the results
# directly as a DataFrame:
#
#       query = "SELECT * FROM INSTRUCTOR"
#       df_result = pd.read_sql(query, conn)
#
# ------------------------
# 1.3. STAFF lab scenario
# ------------------------
# You have a CSV file called INSTRUCTOR.csv with information about
# employees/instructors. The fields are:
#
#   - ID      : Employee identifier
#   - FNAME   : First name
#   - LNAME   : Last name
#   - CITY    : City of residence
#   - CCODE   : Country code (2 letters)
#
# General objective:
#   - Create a STAFF.db database
#   - Create a table named INSTRUCTOR inside that database
#   - Load the CSV data into that table
#   - Run basic queries (SELECT, COUNT)
#   - Insert a new record and verify that it was added
 

import sqlite3
import pandas as pd

# 1) Create / connect to the STAFF.db database
conn = sqlite3.connect("STAFF.db")

# 2) Load CSV data into a DataFrame
df = pd.read_csv(
    "INSTRUCTOR.csv",
    names=["ID", "FNAME", "LNAME", "CITY", "CCODE"]
)

# 3) Create the INSTRUCTOR table and load the CSV data into it
df.to_sql(
    "INSTRUCTOR",
    conn,
    if_exists="replace",
    index=False
)

print("INSTRUCTOR table created and data loaded successfully.\n")

# 4) Run a basic query (SELECT *)
basic1_query = pd.read_sql("SELECT * FROM INSTRUCTOR", conn)
print("SELECT * FROM INSTRUCTOR")
print(basic1_query, "\n")

# 5) Insert a new record
new_row = pd.DataFrame({
    "ID": [100],
    "FNAME": ["John"],
    "LNAME": ["Doe"],
    "CITY": ["Paris"],
    "CCODE": ["FR"]
})

new_row.to_sql("INSTRUCTOR", conn, if_exists="append", index=False)
print("New instructor inserted successfully.\n")

# 6) Count records after insert
count_after = pd.read_sql("SELECT COUNT(*) AS total FROM INSTRUCTOR", conn)
print("Total after insert:", count_after["total"].iloc[0])

# 7) Close the connection
conn.close()
