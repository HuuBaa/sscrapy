# -*- coding: utf-8 -*-

from sqlalchemy import Column,String,Integer,create_engine,Text
from sqlalchemy.ext.declarative import declarative_base

Base=declarative_base()

class Douban(Base):
    __tablename__='douban'

    rank=Column(Integer(),primary_key=True)
    name=Column(String(128))
    score=Column(String(16))
    views=Column(String(64))
    summary=Column(Text())
    

def db_connect():
    engine = create_engine('mysql+pymysql://root:password@localhost:3306/spider?charset=utf8')
    return engine

def create_new_table(engine):
    Base.metadata.create_all(engine)