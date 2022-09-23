import json 
import sqllite3
connection = sqllite3.connect('ja.db')
cursor = connection.cursor()
cursor.execute('Create table if not exists User (name Text,surname Text)')

traffic = json.load(open('json_file.json'))
columns = ['name','course','roll']
for row in traffic:
    keys= tuple(row[c] for c in columns)
    cursor.execute('insert into User values(?,?,?)',keys)
    print(f'{row["name"]} data inserted Succefully')


connection.commit()
connection.clase()