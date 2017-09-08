# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy.loader.processors import Join, MapCompose, TakeFirst

class CsdnItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field(output_processor=TakeFirst())
    link=scrapy.Field(output_processor=TakeFirst())
    posttime=scrapy.Field(output_processor=TakeFirst())
    views=scrapy.Field(output_processor=TakeFirst())
