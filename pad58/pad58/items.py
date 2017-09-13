# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose,Join,TakeFirst
class Pad58Item(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    price=scrapy.Field()   
    area=scrapy.Field()
    urlofpad=scrapy.Field()
    urlofpage=scrapy.Field()

class Pad58ItemLoader(ItemLoader):
	default_item_class=Pad58Item
	default_input_processor=MapCompose(lambda x:x.strip())
	default_output_processor=TakeFirst()






    
