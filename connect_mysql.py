import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database",
)

if connection.is_connected():
    print("Connection successful!")
