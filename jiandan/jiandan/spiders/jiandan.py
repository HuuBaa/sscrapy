# -*- coding: utf-8 -*-

import scrapy
from scrapy import Request
from ..items import JiandanItem
class JiandanSpider(scrapy.Spider):
    name='jiandan'
    allowed_domains=[]
    start_urls=['http://jandan.net/ooxx']

    def parse(self,response):
        item=JiandanItem()
        item['image_urls']=response.css('img::attr(src)').extract()
        yield item
        new_url=response.css('a.previous-comment-page::attr(href)').extract_first()
        if new_url:
            yield Request(new_url,callback=self.parse)

