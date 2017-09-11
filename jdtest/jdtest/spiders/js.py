# -*- coding: utf-8 -*-
import scrapy
import logging

class TestSpider(scrapy.Spider):
    name = "jdtest"
    allowed_domains = ["jd.com"]
    start_urls = [
        "http://www.jd.com/"
    ]
    def parse(self, response):
        logging.info(u'---------我这个是简单的直接获取京东网首页测试---------')
        guessyou = response.xpath('//a[@class="user_profit_lk"]/text()').extract_first()
        logging.info(u"find：%s" % guessyou)
        logging.info(u'---------------success----------------')