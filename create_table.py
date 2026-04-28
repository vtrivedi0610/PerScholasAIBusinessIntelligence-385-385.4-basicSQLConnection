# Before start create psusersdb in MySQL workbench

# Import library
import mysql.connector as mydbconnection
from mysql.connector import Error

# Establish a connection
def connect():
    conn = None

    try:
        conn = mydbconnection.connect(
            database='psusersdb',
            user='root',
            password='root'
        )

        print('Connection Established')
        # Cursor objects allow us to perform SQL operations
        cursor = conn.cursor()

        # Perform SQL operation
        # create a query to use

        myquery2 = "CREATE TABLE `laptop` (`Id` int(11) NOT NULL,\
            `Name` varchar(250) NOT NULL,\
            `Price` float NOT NULL,\
            `Purchase_date` date NOT NULL)"
        
        # Execute query with the cursor.execute() function
        cursor.execute(myquery2)
        print('Right Table Success')

    except Error as e:
        print(f'X Error: {e}')

    finally:
        if conn.is_connected():
            conn.close()
            print('connection Closed')

if __name__ == '__main__':
    connect()