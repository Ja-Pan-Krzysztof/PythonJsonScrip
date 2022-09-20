from sqlite3 import connect


class User:
    def __init__(self, db_name: str) -> None:
        self.db_name = db_name

    def disconn(self):
        return self.conn()\
            .close()

    def conn(self):
        return connect(self.db_name)

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
