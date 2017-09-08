# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from sqlalchemy.orm import sessionmaker
from models import  Douban,create_new_table,db_connect

class DoubanPipeline(object):
    def __init__(self):
        engine=db_connect()
        self.DBSession=sessionmaker(bind=engine)
        session=self.DBSession()
        session.execute('DROP TABLE IF EXISTS douban')
        create_new_table(engine)

    def process_item(self, item, spider):
        movie=Douban(
            rank=item['rank'].encode('utf-8'),
            name=item['name'].encode('utf-8'),
            score=item['score'].encode('utf-8'),
            views=item['views'].encode('utf-8'),
            summary=item['summary'].encode('utf-8'),
            )
        session=self.DBSession()
        session.add(movie)
        session.commit()
        session.close()
