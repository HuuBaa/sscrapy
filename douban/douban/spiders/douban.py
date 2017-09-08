import scrapy
from scrapy import Request
from ..items import DoubanItem

class DoubanSpider(scrapy.Spider):
    name='douban'
    allowed_domains=['douban.com']
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0'}

    def start_requests(self):
        return [Request('https://movie.douban.com/top250',headers=self.headers)]

    def parse(self,response):
        # from scrapy.shell import inspect_response
        # inspect_response(response,self)

        item=DoubanItem()
        movies=response.css('.grid_view li')
        for movie in movies:
            item['rank']=movie.css('.pic em::text').extract()[0]          
            m_name=movie.xpath('.//div[@class="hd"]/a/span[1]/text()').extract()
            m_name+=movie.xpath('.//div[@class="hd"]/a/span[2]/text()').extract()
            m_name+=movie.xpath('.//div[@class="hd"]/a/span[3]/text()').extract()
            item['name']=''.join(m_name)
            item['score']=movie.css('.rating_num::text').extract()[0]
            item['views']=movie.css('.bd .star span:last-child::text').extract()[0]
            summary=movie.css('.quote .inq::text').extract()
            if summary:
                item['summary']=summary[0]
            else:
                item['summary']=''
            yield item

        next_url=response.css('span.next a::attr(href)').extract()
        if next_url:
            next_url=response.urljoin(next_url[0])
            yield Request(next_url,headers=self.headers)