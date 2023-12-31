import mysql.connector

# Replace these with your MySQL server and database information
db_config = {
    "host": "rds-p-1.cuk6nidaykdl.eu-north-1.rds.amazonaws.com",
    "user": "admin",
    "password": "rootroot",
    "database": "ecommerce",
}

# Create a connection to the MySQL server
connection = mysql.connector.connect(**db_config)

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Delete the record with id "d103"
delete_query = """
DELETE FROM products
WHERE id = 'd103'
"""

cursor.execute(delete_query)

# Commit the changes and close the connection
connection.commit()
connection.close()

print("Record with id 'd103' deleted.")
