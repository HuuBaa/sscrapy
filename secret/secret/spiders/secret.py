import scrapy
from ..items import SecretItem

from scrapy_redis.spiders import RedisSpider

class Secretspider(RedisSpider):
    name='secret'
    redis_key='secret:page'

    def parse(self,response):
        item=SecretItem()
        titles=response.css('#ajaxtable tbody:last-child tr')
        for title in titles:
            link=title.css('h3 a::attr(href)').extract_first()
            item['link']=response.urljoin(link)
            yield item


