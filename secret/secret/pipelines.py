# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
from redis import Redis

class SecretPipeline(object):
    def process_item(self, item, spider):
        r=Redis()
        if  item['link']==None and 'htm_data' not in item['link']:
            raise DropItem('drop useless item')
        r.rpush('secret:hei',item['link']) 
        return item
        
