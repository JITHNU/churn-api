import mysql.connector  # MySQL Connector for database connection
import pandas as pd  # Pandas for data handling

# Connect to MySQL Database
conn = mysql.connector.connect(
    host="localhost",  # Change if using a remote MySQL server
    user="root",       # Your MySQL username
    password="yourpassword",  # Replace with your MySQL password
    database="CustomerChurn"  # Your database name
)

cursor = conn.cursor()

cursor.execute("SHOW TABLES;")  # List all tables in the database
tables = cursor.fetchall()
print("Tables in the database:", tables)

conn.close()

