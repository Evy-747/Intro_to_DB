import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Establishing the connection
        connection = mysql.connector.connect(
            host='localhost',  # Change if needed
            user='your_username',  # Replace with your MySQL username
            password='your_password'  # Replace with your MySQL password
        )

        if connection.is_connected():
            print("Connected to MySQL Server")
            
            # Creating a cursor object to execute SQL queries
            cursor = connection.cursor()
            
            # Creating the database if it doesn't already exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error: {e}")
    finally:
        # Closing the connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed")

if __name__ == "__main__":
    create_database()


