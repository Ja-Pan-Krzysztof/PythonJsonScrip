#Exceptions
from pymysql import err
from sqlalchemy import exc

import logging.config

from dotenv import load_dotenv
from os import getenv

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database


logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)

load_dotenv()

HOST = '127.0.0.1'
PORT = 3306
DATABASE = 'users_praktyki'
URL = f'mysql+pymysql://{getenv("_USER")}:{getenv("_PASS")}@localhost/{DATABASE}'


ENGINE = create_engine(URL,
                       connect_args=dict(host=HOST, port=PORT),
                       pool_recycle=600,
                       echo=True,
                       )


'''Create session'''
Session = sessionmaker(bind=ENGINE)


'''Connect to mysql database'''


def start_mysql() -> tuple:
    try:
        logger.debug(f'Login MySQL - [{HOST}:{PORT}] - processing...')

        if not database_exists(URL):
            create_database(URL)

        conn = ENGINE.connect()

        session = Session()
        logger.info(f'Login MySQL - [{HOST}:{PORT}] - Success !')

        return 0, conn, session, ENGINE

    except (ConnectionRefusedError, err.OperationalError, exc.OperationalError) as e:
        logger.error(f'Can\'t connect to @[{HOST}:{PORT}]')

        logger.error(f'Login MySQL - [{HOST}:{PORT}] - Falied !')

        return 1, e
