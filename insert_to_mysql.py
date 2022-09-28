from database_mysql import BASE, session

from sqlalchemy import Column, String, Integer

from typing import NoReturn


class Users(BASE):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    surname = Column(String(255))

    def __init__(self, name, surname):
        """ Takes parameters as strings

        :param name: name
        :param surname: surname
        """
        self.name = name
        self.surname = surname


def insert_record(name: str, surname: str) -> NoReturn:
    users = Users(name, surname)

    '''Add data to table / save / disconnect'''
    session.add(users)
    session.commit()
    session.close()
