import scrapy
from ..items import Secret2Item
import logging
from scrapy_redis.spiders import RedisSpider


class Secretspider2(RedisSpider):
    name='secret2'
    redis_key='secret:hei'
    def parse(self,response):
        item=Secret2Item()
        item['image_urls']=response.css('div.tpc_content input::attr(src)').extract()
        logging.info(item['image_urls'])
        yield item
