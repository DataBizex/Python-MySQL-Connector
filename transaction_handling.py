import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database",
)
cursor = connection.cursor()

try:
    cursor.execute(
        """
    INSERT INTO employees (name, position, salary)
    VALUES (%s, %s, %s)
    """,
        ("Jane Smith", "Data Scientist", 90000),
    )
    connection.commit()

except mysql.connector.Error as err:
    print(f"Error: {err}")
    connection.rollback()
