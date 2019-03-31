import pyodbc
import pandas as pd 

connection = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER=localhost;UID=userdev;PWD=Halls12345$')

if connection:
    print("Yes we are connected")
else:
    print("Not connected")
cursor = connection.cursor()
cursor.execute('select  * from spt_monitor')

--for row in cursor:
--print('My Records = %r' % (row))
columns = [desc[0] for desc in cursor.description]
data =  cursor.fetchall()
df = pd.DataFrame(list(data),columns=columns)

writer= pd.ExcelWriter('foo.xlsx')
df.to_excel(writer,sheet_name='bar')
writer.save()



