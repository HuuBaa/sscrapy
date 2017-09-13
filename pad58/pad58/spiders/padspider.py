import scrapy
from ..items import Pad58ItemLoader
from redis import Redis
from scrapy_redis.spiders import RedisSpider
import logging
from time import sleep

class MySpider(RedisSpider):
	name='myspider_pads'
	redis_key='myspider:pad_urls'

	def parse(self,response):
		el=Pad58ItemLoader(response=response)
		el.add_css('title','.info_titile::text')
		el.add_css('price','.price_now i::text')
		el.add_css('area','div.palce_li span i::text')
		el.add_value('urlofpad',response.url)
		return el.load_item()
