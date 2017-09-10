import scrapy
import json
from scrapy import Request
from ..items import DoubanAjaxItem

class DoubanAjaxSpider(scrapy.Spider):
    name='douban_ajax'
    allowed_domains=['douban.com']
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0'}
    page_num=0
    url='https://movie.douban.com/j/chart/top_list?type=5&interval_id=100:90&action=&start={0}&limit=20'
    def start_requests(self):
        
        yield Request(self.url.format(self.page_num),headers=self.headers)

    def parse(self,response):
        item=DoubanAjaxItem()
        datas=json.loads(response.body)
        if datas:
            for data in datas:
                item['rank']=data['rank']
                item['movie_name']=data['title']
                item['score']=data['score']
                item['votes']=data['vote_count']
                yield item

            self.page_num+=20
            yield Request(self.url.format(self.page_num),headers=self.headers)


