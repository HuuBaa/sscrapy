# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem

from sqlalchemy import Column,String,Integer,create_engine,Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import logging
class CleanPipeline(object):

    def __init__(self):
        self.has=set()

    def process_item(self, item, spider):
        if len(item.keys())>=4:
            if item in self.has:
                raise DropItem('Duplicate item droped %s'%item)
            else:
                self.has.add(item)
                return item
        else:
            raise DropItem('Useless item droped %s'%item)


Base=declarative_base()

class Pads(Base):
    __tablename__='pads'

    id=Column(Integer(),primary_key=True)
    title=Column(Text())
    price=Column(String(64))
    area=Column(String(64))
    url=Column(Text())


def db_connect():
    engine = create_engine('mysql+pymysql://root:password@localhost:3306/spider?charset=utf8')
    return engine

def create_new_table(engine):
    Base.metadata.create_all(engine)


class SqlPipeline(object):

    def __init__(self):
        engine=db_connect()
        self.DBSession=sessionmaker(bind=engine)
        # session=self.DBSession()
        # session.execute('DROP TABLE IF EXISTS pads')
        create_new_table(engine)

    def process_item(self, item, spider):
        pad=Pads(
            title=item['title'].encode('utf-8'),
            price=item['price'].encode('utf-8'),
            area=item['area'].encode('utf-8'),
            url=item['urlofpad'].encode('utf-8')           
            )
        session=self.DBSession()
        session.add(pad)
        session.commit()
        session.close()



