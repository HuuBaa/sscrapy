# -*- coding: utf-8 -*-
import scrapy
from ..items import BaihehuaItem


class GetSpider(scrapy.Spider):
    name = 'get'
    allowed_domains = ['myfreejav.club','cache.baiducontent.com']
    start_urls = ['http://www.myfreejav.club/cn/vl_star.php?&mode=&s=aznus&page=2/']



    def parse(self, response):
        baihehuas = []
        a_list=response.css(".videos .video")
        for a in a_list:
            baihehua = BaihehuaItem()
            baihehua['title']=a.css("a::attr(title)").extract_first()
            baihehua['image'] =a.css("a div::text").extract_first()
            baihehua['number'] =a.css("a img::attr(src)").extract_first()

        return baihehuas
