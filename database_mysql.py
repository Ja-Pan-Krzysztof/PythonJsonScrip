from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, String, Integer


'''Construct a base class'''
BASE = declarative_base()

'''Connect to mysql database'''
ENGINE = create_engine('mysql+pymysql://root:admin@localhost/users_praktyki',
                       connect_args=dict(host='127.0.0.1', port=3306))

'''Create session'''
Session = sessionmaker(bind=ENGINE)
session = Session()
