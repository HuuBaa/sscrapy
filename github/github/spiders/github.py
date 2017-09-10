# -*- encoding: utf-8 -*-

import logging
import sys
import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request,FormRequest,HtmlResponse

# logging.basicConfig(level=logging.INFO,
#                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                     datefmt='%Y-%m-%d %H:%M:%S',
#                     handlers=[logging.StreamHandler(sys.stdout)])

class GithubSpider(CrawlSpider):
    name='github'
    allowed_domains=['github.com']
    start_urls=['https://github.com/issues']

    rules=[
        Rule(LinkExtractor( allow= (r'/issues/\d+',) , restrict_css='ul li div div:nth-child(3) a:nth-child(2)' ),callback='parse_page' )

    ]

    posts_headers={
    'Host': 'github.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/x-www-form-urlencoded',
   ' Referer': 'https://github.com/',
    'Connection': 'keep-alive'
    }

    def start_requests(self):
        return [Request('https://github.com/login',meta={'cookiejar':1},callback=self.parse_login)]

    def parse_login(self,response):
        authenticity_token=response.css('form input[name="authenticity_token"]::attr(value)').extract_first()
        logging.info('authenticity_token:'+authenticity_token)
        return [FormRequest.from_response(
                    response,
                    url='https://github.com/session',
                    headers=self.posts_headers,
                    meta={'cookiejar':response.meta['cookiejar']},
                    formdata={
                        'commit':'Sign+in',
                        'utf8':'✓',
                        'authenticity_token':authenticity_token,  
                        'login':'742790905@qq.com',
                        'password':'*****'
                    },
                    callback=self.after_login,
                    dont_filter=True
                     )]

    def after_login(self,response):
        for url in self.start_urls:
            # 因为我们上面定义了Rule，所以只需要简单的生成初始爬取Request即可
            yield Request(url, meta={'cookiejar': response.meta['cookiejar']})

    def parse_page(self,response):
        logging.info(u'--------------消息分割线-----------------')
        logging.info(response.url)
        issue_title = response.xpath(
            '//span[@class="js-issue-title"]/text()').extract_first()
        logging.info(u'issue_title:' + issue_title.encode('utf-8'))


    # def _requests_to_follow(self, response):
    #     """重写加入cookiejar的更新"""
    #     if not isinstance(response, HtmlResponse):
    #         return
    #     seen = set()
    #     for n, rule in enumerate(self._rules):
    #         links = [l for l in rule.link_extractor.extract_links(response) if l not in seen]
    #         if links and rule.process_links:
    #             links = rule.process_links(links)
    #         for link in links:
    #             seen.add(link)
    #             r = Request(url=link.url, callback=self._response_downloaded)
    #             # 下面这句是我重写的
    #             r.meta.update(rule=n, link_text=link.text, cookiejar=response.meta['cookiejar'])
    #             yield rule.process_request(r)