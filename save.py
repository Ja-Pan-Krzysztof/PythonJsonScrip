import json 
#importuje json
import sqlite3
#impoeruje sqlite3
from database import User


connection = sqlite3.connect('ja.db')
#polacza sie z baza danych 
cursor = connection.cursor()
# cursor.execute('Create table if not exists user (name Text,surname Text)')

traffic = json.load(open('json_file.json'))
#otwiera json
columns = ['name', 'course', 'roll']

for row in traffic:
    keys= tuple(row[c] for c in columns)
    cursor.execute('insert into User values(?,?,?)',keys)
    print(f'{row["name"]} data inserted Succefully')
    #pisze


connection.commit()
connection.close()
#zamyka poloczenie 


################

u = User('user', 'user.db')
#xD
u.conn()
#u.insert_sercords("", "")
u.disconn()
#dziala tak troche <-: