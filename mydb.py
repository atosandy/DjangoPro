import mysql.connector


dataBase = mysql.connector.connect(
    host='localhost',
    user='root', 
    passwd='Good2024',
)


#prepare a cursor object
cursorObject = dataBase.cursor()

#Create a database
cursorObject.execute("CREATE DATABASE vcc")

print("All Done!")