import mysql.connector
from mysql.connector import Error
from dbase_creds import host, user, password, database

def test_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        if connection.is_connected():
            db_info = connection.get_server_info()
            print(f"Connected successfully. MySQL server version: {db_info}")

            cursor = connection.cursor()
            cursor.execute("SELECT DATABASE();")
            record = cursor.fetchone()
            print(f"Connected to database: {record[0]}")
            cursor.close()

    except Error as e:
        print(f"Failed to connect to MySQL: {e}")

    finally:
        if connection is not None and connection.is_connected():
            connection.close()
            print("Connection closed.")

if __name__ == "__main__":
    test_connection()
