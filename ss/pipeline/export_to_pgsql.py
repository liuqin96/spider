#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/17 21:57
# @Author  : SmallStrong
# @Des     : 
# @File    : export_to_pgsql.py
# @Software: PyCharm


from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import QueuePool
import logging
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, Boolean, Unicode, SmallInteger, BigInteger, Numeric, Float, DateTime, \
    Date, Time, \
    Binary, LargeBinary

PGSQL = {
    'HOST': 'localhost',
    'PORT': '5432',
    'USER': 'small',
    'PASSWORD': 'smallstrong',
    'DATABASE': 'db_name',
}

Base = declarative_base()

conn = 'postgresql+psycopg2://{}:{}@{}:{}/{}'.format(PGSQL['USER'], PGSQL['PASSWORD'], PGSQL['HOST'], PGSQL['PORT'],
                                                     PGSQL['DATABASE'])
engine = create_engine(conn, pool_size=10, pool_recycle=500, pool_timeout=30, pool_pre_ping=True, max_overflow=0,
                       poolclass=QueuePool)
Session = sessionmaker(bind=engine)


class cli:
    def __init__(self):
        self.session = Session()

    def con_commit_close(self, func):
        def wrapper(*args, **kw):
            try:
                func(*args, **kw)
                self.session.commit()
            except Exception as e:
                self.session.rollback()
                logging.error(e.message)
            finally:
                self.session.close()

        return wrapper


def test(bean):
    rds = cli()
    session = rds.session
    session.add(bean)
    session.commit()


############################
# 数据结构与建表
############################
class User(Base):
    __tablename__ = 'user'

    user_id = Column(Integer(), primary_key=True, unique=True, nullable=False)
    name = Column(String(20))


def create_table():
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    create_table()
    test(User(user_id=10, name='small'))
