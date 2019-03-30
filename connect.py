import pyodbc

connection = pyodbc.connect("DSN=USER-PC,autocommit=True")

if connection:
    print("Yes we are connected")
else:
    print("Not connected")


