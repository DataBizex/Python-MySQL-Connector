import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database",
)
cursor = connection.cursor()

cursor.execute("SELECT * FROM employees")
results = cursor.fetchall()

for row in results:
    print(row)
