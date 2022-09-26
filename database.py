from sqlite3 import connect


class User:
    def __init__(self, db_name: str, db) -> None:
        self.db_name = db_name
        self.db = db

    def disconn(self):
        return self.conn()\
            .close()

    def conn(self):
        return connect(self.db)

    def create_table(self):
        script = f'''CREATE TABLE IF NOT EXISTS {self.db_name} (
            name varchar(255),
            surname varchar(255)
        );
        '''

        self.conn()\
            .cursor()\
            .execute(script)

        self.conn()\
            .commit()

    def insert_sercords(self, name: str, surname: str):
        sql = f'INSERT INTO {self.db_name} (name, surname) VALUES ("{name}, "{surname}"'

        self.conn()\
            .cursor()\
            .execute(sql)

        self.conn()\
            .commit()
