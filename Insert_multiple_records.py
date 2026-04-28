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

        print('Established DB connection')


        mySql_insert_query = """INSERT INTO Laptop (Id, Name, Price, Purchase_date) 
                           VALUES (%s, %s, %s, %s) """

        records_to_insert = [
                        (4, 'HP Pavilion Power', 1999, '2019-01-11'),
                        (5, 'MSI WS75 9TL-496', 5799, '2019-02-27'),
                        (6, 'Microsoft Surface', 2330, '2019-07-23')
        ]
        cursor = conn.cursor()
        cursor.executemany(mySql_insert_query, records_to_insert)
        conn.commit()
        print(f' {cursor.rowcount}: Records successfully added to Laptop table')

        
    except Error as e:
        print(f'X Error: {e}')

    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print('Db connection closed')

if __name__ == '__main__':
    connect()