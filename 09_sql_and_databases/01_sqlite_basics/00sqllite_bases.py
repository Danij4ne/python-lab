



import psycopg2  # PostgreSQL (ejemplo)

#  CONNECT
conn = psycopg2.connect(
    host="localhost",
    database="company",
    user="admin",
    password="1234"
)

# CREATE CURSOR (canal de comunicación)
cursor = conn.cursor()

# SEND + EXECUTE
cursor.execute("UPDATE employees SET salary = salary * 1.1")

# COMMIT / STATUS
conn.commit()

# DISCONNECT
cursor.close()
conn.close()


#MySQL       → mysql-connector / pymysql
#PostgreSQL  → psycopg2
#IBM DB2     → ibm_db
#SQL Server  → pyodbc (ODBC)
#Windows DB  → ODBC
#MongoDB → PyMongo

