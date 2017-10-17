from selenium import webdriver
import os
import time
from pyquery import PyQuery as pq
def login_weibo():
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
        body=driver.page_source
        doc=pq(body)
        follows=doc('.follow_item ')
        for follow in follows.items():
            name=follow('a.S_txt1').text()
            sex=follow('div.info_name a:last').find('i').attr('class').split('_')[-1]
            following=follow('div.info_connect span').eq(0).find('a').text()
            followed=follow('div.info_connect span').eq(1).find('a').text()
            weibo_count=follow('div.info_connect span').eq(2).find('a').text()
            print(name,sex,following,followed,weibo_count)
        js="var q=document.documentElement.scrollTop={}"
        driver.execute_script(js.format(15000))
        elem_next=driver.find_element_by_css_selector("a.next")
        elem_next.click()         
        if elem_next.get_attribute("href") is None:
            break
        time.sleep(3)
    
    print('end')


if __name__ == '__main__':
    login_weibo()
    
# ?access_token=2.00GpndZDajPDpCf21f93395671ibvB



