import mysql.connector
 
#+-----------------------------------------------+
#| dbase credential                              |
host = "localhost"
user = "root"
password = "Hewasborn@1889"
database = "medicOpenX"
#+-----------------------------------------------+

def get_db_connection():
    return mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
