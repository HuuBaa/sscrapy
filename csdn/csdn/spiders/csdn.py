# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors import LinkExtractor


from ..items import CsdnItem
from scrapy.loader import ItemLoader

nextpage=u'x下一页'
class CsdnSpider(CrawlSpider):
    name='csdn'
    allowed_domains=['csdn.net']
    start_urls=['http://blog.csdn.net/qq_35037977/article/list/1']
    rules=[
            Rule(LinkExtractor(allow=r'/qq_35037977/article/list/\d+',restrict_xpaths="//a[contains(., %s)]"%nextpage),follow=True),
            Rule(LinkExtractor(allow=r'/qq_35037977/article/details/\d+',restrict_css='.link_title'),callback='parse_csdn')
    ]


    def parse_csdn(self,response):
        l=ItemLoader(item=CsdnItem(),response=response)
        l.add_css('title','#article_details .link_title a::text')
        l.add_value('link',response.url)
        l.add_css('posttime','.article_r .link_postdate::text')
        l.add_css('views','.article_r .link_view::text')
        return l.load_item()


