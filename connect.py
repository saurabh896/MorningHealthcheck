import pyodbc

connection = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER=localhost;UID=userdev;PWD=Halls12345$')

if connection:
    print("Yes we are connected")
else:
    print("Not connected")
cursor = connection.cursor()
cursor.execute('select  * from spt_monitor')

for row in cursor:
    print('My Records = %r' % (row))

