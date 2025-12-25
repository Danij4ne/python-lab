
# DATABASE CONNECTIONS & CURSORS (Python DB-API)

# 1) CONNECTION OBJECTS
 
# Connection objects are used to connect to a database
# and manage transactions.
#
# They control:
# - Opening and closing the database
# - Saving changes (commit)
# - Reverting changes (rollback)

"""
.cursor()    -> Creates and returns a new Cursor object
.commit()    -> Saves (commits) all pending transactions
.rollback()  -> Reverts all pending transactions
.close()     -> Closes the database connection
"""

# 2) CURSOR OBJECTS
 
# Cursor objects are used to:
# - Execute SQL queries
# - Read results returned from the database
#
# A cursor is created from a connection and works as the
# interface between Python and SQL.


# 3) CURSOR METHODS
 

# .execute()
# Executes a single SQL statement
cursor.execute("SELECT * FROM users")


# .executemany()
# Executes the same SQL statement many times
# (typically used for bulk INSERTs)

data = [
    ("Ana", 25),
    ("Luis", 30),
    ("Maria", 28)
]

cursor.executemany(
    "INSERT INTO users (name, age) VALUES (?, ?)",
    data
)


# .fetchone()
# Returns one row from the result set

cursor.execute("SELECT * FROM users")
row = cursor.fetchone()


# .fetchmany()
# Returns multiple rows from the result set

cursor.execute("SELECT * FROM users")
rows = cursor.fetchmany(3)


# .fetchall()
# Returns all rows from the result set

cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()


# .callproc()
# Executes a stored procedure

cursor.callproc("get_users")


# .nextset()
# Moves to the next result set
# (when a stored procedure returns multiple SELECTs)

cursor.nextset()
rows = cursor.fetchall()


# .arraysize
# Defines how many rows fetchmany() returns by default

cursor.arraysize = 5
rows = cursor.fetchmany()


# .close()
# Closes the cursor and releases resources

cursor.close()


# 4) TYPICAL DATABASE WORKFLOW IN PYTHON
 

from dbmodule import connect   # import connect() from a DB module

# 1 - Create a connection
connection = connect("databasename", "username", "password")

# 2 - Create a cursor from the connection
cursor = connection.cursor()

# 3 - Execute a query
cursor.execute("SELECT * FROM mytable")

# 4 - Fetch results
results = cursor.fetchall()

# 5 - Close everything
cursor.close()
connection.close()
