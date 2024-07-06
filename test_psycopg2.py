import psycopg2

try:
    connection = psycopg2.connect(database="your_database_name", user="your_username", password="your_password", host="your_host")
    print("Connection successful!")
except Exception as e:
    print(f"Error connecting to database: {e}")

finally:
    if connection:
        connection.close()
