# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanAjaxItem(scrapy.Item):
    # define the fields for your item here like:
    rank = scrapy.Field()
    movie_name = scrapy.Field()
    score = scrapy.Field()
    votes = scrapy.Field()

