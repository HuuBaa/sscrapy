# -*- coding: utf-8 -*-

import scrapy
import logging
from scrapy_splash import SplashRequest

class JsSpider(scrapy.Spider):
    name = "splashtest"
    allowed_domains = ["jd.com"]
    start_urls = [
        "http://www.jd.com/"
    ]
    def start_requests(self):
        splash_args = {
            'wait': 0.5,
        }
        for url in self.start_urls:
            yield SplashRequest(url, self.parse_result, endpoint='render.html',
                                args=splash_args)
    def parse_result(self, response):
        logging.info(u'----------使用splash爬取京东网首页异步加载内容-----------')
        newer = response.xpath('//a[@class="user_profit_lk"]/text()').extract_first()
        logging.info(u"find：%s" % newer)
        logging.info(u'---------------success----------------')