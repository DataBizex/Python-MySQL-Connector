import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database",
)
cursor = connection.cursor()

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    position VARCHAR(255) NOT NULL,
    salary DECIMAL(10, 2)
)
"""
)

connection.commit()
