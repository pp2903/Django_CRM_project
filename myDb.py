import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'user1',
    passwd = 'l1e2m3o4n5'
)

cursorObject = dataBase.cursor()

cursorObject.execute('CREATE DATABASE siteDb')

print('Database created!! ')