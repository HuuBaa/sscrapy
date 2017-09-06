# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from sqlalchemy.orm import sessionmaker
from models import  Article,create_new_table,db_connect


class HuxiuPipeline(object):
    def __init__(self):
        engine=db_connect()
        self.DBSession=sessionmaker(bind=engine)
        session=self.DBSession()
        session.execute('DROP TABLE IF EXISTS article')
        create_new_table(engine)

    def process_item(self, item, spider):
        art=Article(
            title=item['title'].encode('utf-8'),
            link=item['link'].encode('utf-8'),
            posttime=item['posttime'].encode('utf-8'),
            body=item['body'].encode('utf-8'),
            source_site=item['source_site'].encode('utf-8')
            )
        session=self.DBSession()
        session.add(art)
        session.commit()
        session.close()
