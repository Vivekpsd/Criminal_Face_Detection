import mysql.connector
conn = mysql.connector.connect(host='localhost', password='password', user='root')

if conn.is_connected():
    print("Connected")