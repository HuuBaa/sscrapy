# -*- coding: utf-8 -*-
import scrapy

class SeleniumSpider(scrapy.Spider):
    name='seleniumtest'
    start_urls=['https://www.jd.com/']

    def parse(self,response):
        f=open('jd.html','w',encoding='utf-8')
        print(response.body.decode('utf-8'),file=f)
        newer=response.css('.user_profit_lk::text').extract_first()
        print(newer)