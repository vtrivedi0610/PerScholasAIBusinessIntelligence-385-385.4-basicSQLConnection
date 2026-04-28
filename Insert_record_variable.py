# Import Libraries
import mysql.connector as mydbconnection
from mysql.connector import Error

def connect(id, name, price, purchase_date):
    conn = None

    try:

        conn = mydbconnection.connect(
            database='psusersdb',
            user='root',
            password='root'
        )

        print('Established DB connection')

        cursor = conn.cursor()

        mySql_insert_query = """INSERT INTO Laptop (Id, Name, Price, Purchase_date)VALUES (%s, %s, %s, %s) """

        record = (id, name, price, purchase_date)

        cursor.execute(mySql_insert_query, record)
        conn.commit()
        print('Right Records successfully added to Laptop table')

    except Error as e:
        print(f'X Error: {e}')

    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print('Db connection closed')

if __name__ == '__main__':
    connect(23, 'HP Laptop', 5000, '2026-01-01')
    connect(24, 'Chromebook', 6000, '2026-03-01')