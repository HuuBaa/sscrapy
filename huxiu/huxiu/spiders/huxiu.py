# _*_ encoding: utf-8 _*_

from ..items import HuxiuItem
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

class HuxiuSpider(CrawlSpider):
    name='huxiu'
    allowed_domains=['huxiu.com']
    start_urls=['https://www.huxiu.com/']

    rules=[
            Rule(LinkExtractor(allow=(r'/article/\d+\.html',)),callback='parse_article')
    ]

    # def parse(self,response):
    #     for sel in response.css('.mod-info-flow .mod-art .mob-ctt'):
    #         item=HuxiuItem()          
    #         link=sel.css('h2 a::attr(href)')[0].extract()
    #         item['link']=response.urljoin(link)
    #         yield scrapy.Request(item['link'],callback=self.parse_article)

    def parse_article(self,response):
        item=HuxiuItem()
        body_text=''
        item['title']=response.css('.article-wrap h1::text')[0].extract().replace('\r','').strip()
        item['link']=response.url
        item['posttime']=response.css('.article-wrap .article-author span.article-time::text')[0].extract()
        body=response.css('.article-wrap .article-content-wrap')
        item['source_site']="".join(body.css('p:first-child span::text').extract())
        for p in body.css('p::text'):
            p_text=p.extract()
            body_text+=p_text
        item['body']=body_text
        yield item