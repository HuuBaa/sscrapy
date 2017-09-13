import scrapy
from ..items import Pad58ItemLoader
from redis import Redis
from scrapy_redis.spiders import RedisSpider
import logging
from time import sleep

class MyUrlSpider(RedisSpider):
	name='myspider_urls'
	redis_key='myspider:urls'
	
	def parse(self,response):
		el=Pad58ItemLoader(response=response)
		r=Redis()
		logging.info(response.url)
		urls=response.css('.tbimg tr.zzinfo')
		for url in urls:
			pad_url=url.css('td.t a.t::attr(href)').extract_first()
			if pad_url != '' and 'jump' not in pad_url:
				r.lpush('myspider:pad_urls',pad_url)

		pageurl=response.css('a.next::attr(href)').extract_first()
		pageurl=response.urljoin(pageurl)
		# logging.info(pageurl)
		
		if pageurl !='':
			r.lpush('myspider:urls',pageurl)
			sleep(1)
			el.add_value('urlofpage',pageurl)
		return el.load_item()




