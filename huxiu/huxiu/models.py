# -*- coding: utf-8 -*-

from sqlalchemy import Column,String,Integer,create_engine,Text
from sqlalchemy.ext.declarative import declarative_base

Base=declarative_base()

class Article(Base):
    __tablename__='article'

    id=Column(Integer(),primary_key=True)
    title=Column(String(64))
    posttime=Column(String(16))
    link=Column(String(64))
    source_site=Column(Text())
    body=Column(Text())

def db_connect():
    engine = create_engine('mysql+pymysql://root:password@localhost:3306/spider?charset=utf8')
    return engine

def create_new_table(engine):
    Base.metadata.create_all(engine)