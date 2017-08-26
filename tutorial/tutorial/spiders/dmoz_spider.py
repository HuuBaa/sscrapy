import scrapy
from tutorial.items import DmozItem,ArticleItem
class DmozSpider(scrapy.Spider):
    name="csdn"
    allowed_domains=["csdn.net"]
    start_urls=[
    "http://blog.csdn.net/qq_35037977/article/list/1",
    "http://blog.csdn.net/qq_35037977/article/list/2",
    "http://blog.csdn.net/qq_35037977/article/list/3",
    ]
    def parse(self,response):
        for href in response.css("span.link_title a::attr(href)"):
            url=response.urljoin(href.extract())
            yield scrapy.Request(url,callback=self.parse_article)

    def parse_article(self,response):
            item=ArticleItem()
            item['view']=response.css(".link_view::text").extract()[0]
            item['title']=response.css(".link_title a::text").extract()[0].strip()
            yield item

