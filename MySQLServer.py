#!/usr/bin/python3
import mysql.connector

def create_database():
    connection = None
    try:
        # CONNECT TO MYSQL SERVER
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""  # CHANGE IF YOUR MYSQL HAS A PASSWORD
        )

        cursor = connection.cursor()

        # CREATE DATABASE (NO SELECT OR SHOW USED)
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        print(f"Error while connecting to MySQL: {err}")

    finally:
        # CLOSE CONNECTION
        if connection is not None and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()

