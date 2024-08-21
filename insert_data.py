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
INSERT INTO employees (name, position, salary)
VALUES (%s, %s, %s)
""",
    ("John Doe", "Software Engineer", 75000),
)

connection.commit()
