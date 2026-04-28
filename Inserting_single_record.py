# Import libraries
import mysql.connector as mydbconnection
from mysql.connector import Error

def connect():
    conn = None

    try:

        conn = mydbconnection.connect(
            database='psusersdb',
            user='root',
            password='root'
        )

        print('Connect to SQL DB')

        cursor = conn.cursor()

        mySql_insert_query = """INSERT INTO Laptop (Id, Name, Price, Purchase_date) 
                           VALUES (30, 'Router', 65000, '2022-08-14') """
        
        cursor.execute(mySql_insert_query)
        conn.commit()
        print(cursor.rowcount, "Right REcord inserted successfully into laptop table")

        cursor.close()

    except Error as e:
        print(f'X Error: {e}')

    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print('Db connection closed')

if __name__ == '__main__':
    connect()