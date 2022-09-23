import json 
import sqlite3

from database import User


connection = sqlite3.connect('ja.db')
cursor = connection.cursor()
# cursor.execute('Create table if not exists user (name Text,surname Text)')

traffic = json.load(open('json_file.json'))
columns = ['name','course','roll']
for row in traffic:
    keys= tuple(row[c] for c in columns)
    cursor.execute('insert into User values(?,?,?)',keys)
    print(f'{row["name"]} data inserted Succefully')


connection.commit()
connection.close()


################

u = User('user', 'user.db')
u.conn()

u.insert_record(1, 2)
u.disconn()
