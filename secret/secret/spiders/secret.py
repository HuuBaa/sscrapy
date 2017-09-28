import scrapy
from ..items import SecretItem
import logging
# from scrapy_redis.spiders import RedisSpider
# from redis import Redis
class Secretspider(scrapy.Spider):
    name='secret'
    start_urls=['%s'%count for count in range(2,11)]
    
    def parse(self,response):
        
        item=SecretItem()
        titles=response.css('#ajaxtable tbody:last-child tr')
        for title in titles:
            link=title.css('h3 a::attr(href)').extract_first()
            item['link']=response.urljoin(link)
            yield item

        # next_page=response.xpath("//a[contains(.,'下一頁')]/@href").extract_first()
        # next_page=response.urljoin(next_page)
        # r.rpush('secret:page',next_page)
        # logging.info('下一页'+next_page)
        #return scrapy.Request(next_page,callback=self.parse)


