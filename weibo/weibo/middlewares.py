# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html
from selenium import webdriver
import os
import time
from scrapy import signals
from scrapy.http import HtmlResponse
class WeiboSpiderDownlaodMiddleware(object):
    def process_request(self,request,spider):
        driver=webdriver.Firefox()
        driver.get('http://weibo.com/')
        time.sleep(10)

        elem_user = driver.find_element_by_name("username")
        elem_user.click()
        elem_user.send_keys(os.environ.get('WEIBO_USER')) #用户名  
        elem_pwd = driver.find_element_by_name("password")  
        elem_pwd.send_keys(os.environ.get('WEIBO_PASS'))  #密码  

        elem_sub = driver.find_element_by_css_selector('.login_btn a')  
        elem_sub.click()              #点击登陆  
        time.sleep(5)
        elem_fans=driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[3]/div[2]/div[2]/div[2]/div/div/div[2]/ul/li[2]/a")
        elem_fans.click()
        time.sleep(3) 
        while True:
            js="var q=document.documentElement.scrollTop={}"
            driver.execute_script(js.format(15000))
            elem_next=driver.find_element_by_css_selector("a.next")
            elem_next.click() 
            time.sleep(3)
            body=driver.page_source
            return HtmlResponse(driver.current_url,body=body,encoding='utf-8',request=request)       
            if elem_next.get_attribute("href") is None:
                break
            

class WeiboSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
