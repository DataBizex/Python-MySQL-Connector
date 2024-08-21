# Connecting to MySQL:
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database"
)

# Creating a Table:
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    position VARCHAR(255) NOT NULL,
    salary DECIMAL(10, 2)
)
""")

# Inserting Data:
cursor.execute("""
INSERT INTO employees (name, position, salary)
VALUES (%s, %s, %s)
""", ("John Doe", "Software Engineer", 75000))

connection.commit()

# Fetching Data:
cursor.execute("SELECT * FROM employees")
results = cursor.fetchall()

for row in results:
    print(row)

# Handling Transactions:
try:
    cursor.execute("""
    INSERT INTO employees (name, position, salary)
    VALUES (%s, %s, %s)
    """, ("Jane Smith", "Data Scientist", 90000))
    connection.commit()

except mysql.connector.Error as err:
    print(f"Error: {err}")
    connection.rollback()
