from database_mysql import start_mysql

from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

from typing import NoReturn
import logging.config


logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)


BASE = declarative_base()


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
    """Insert record to Users

    :param name: string
    :param surname: string
    :return: NoReturn
    """

    try:
        users = Users(name, surname)

        status, conn, session, engine = start_mysql()
        BASE.metadata.create_all(engine)

        session.add(users)
        session.commit()

        conn.close()

        return 0

    except Exception as e:
        logger.error('Can\'t add record.')
        raise e

