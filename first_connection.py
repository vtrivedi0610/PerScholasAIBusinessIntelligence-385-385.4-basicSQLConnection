# Import Library
import mysql.connector as mydbconnection
from mysql.connector import Error

def connect():
# Establish connection
    conn = None

    try:
        conn = mydbconnection.connect(database='classicmodels', user='root', password='root')
# Perform SQL Operations
        if conn.is_connected():
            print('Connected to MySQL DB')

    except Error as e:
        print(f'X Error: {e}')

    finally: # runs whether operation failed or not (Always runs)
        # close our connection
        if conn is not None and conn.is_connected():
            conn.close()
            print('DB connection Closed')


if __name__ == '__main__':
    connect()