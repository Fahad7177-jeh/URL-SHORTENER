import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="url_shortener"
)

cursor = connection.cursor()
if connection.is_connected():
    print("MySQL Connected Successfully!")