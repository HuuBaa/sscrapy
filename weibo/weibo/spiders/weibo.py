import scrapy
from selenium import webdriver
from scrapy.http import HtmlResponse
import time
class WeiboSpider(scrapy.Spider):
    name='weibo'
    start_urls=['http://weibo.com/']
    def parse(self,response):
        print(response.url)
       
        
        






