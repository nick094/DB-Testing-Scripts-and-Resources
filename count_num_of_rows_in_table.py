import mysql.connector
from mysql.connector import Error  

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='python_db',
                                         user='root',
                                         password='')
    
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("SELECT count(*) from customers") # select the table
        records = cursor.fetchall()
        print(records)

except Error as e:

    print ("Unable to count", e)

finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

