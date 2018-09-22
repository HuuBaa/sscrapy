#!/usr/bin/env python
#-*- coding: utf-8 -*-

from pyquery import PyQuery as pq
import requests
from urllib import request

def get(url):
    res=requests.get(url)
    page=pq(res.text)

    for av in page(".videos .video a"):
        number=pq(av)("div.id").text()
        img=pq(av)("img").attr("src")
        if img and number:
            try:
                request.urlretrieve('http:'+img,'F:/sscrapy/baihehua/avs/%s.jpg'%number)
            except:
                pass

get('http://www.myfreejav.club/cn/vl_star.php?&mode=&s=aznus&page=2')
# get('http://cache.baiducontent.com/c?m=9f65cb4a8c8507ed4fece763105392230e54f73c77839042288cc00c84642c101921b3a6767e0d408dd27b1340e91a1cfdf041306d4137b6ef899f4babe8da7468c933712d5cd04e05a31bb8bd4d32b153872b9db81897ad8138e0&p=c3759a45d6c200ea0abe9b7c484895&newp=c4759a45d6c21afb1c81c7710f05a5231610db2151d7d6116b82c825d7331b001c3bbfb423251001d6c07a6205a9485fe8f5367433012ba3dda5c91d9fb4c57479d373701c&user=baidu&fm=sc&query=%B0%D9%BA%CF%C8A&qid=caa292a300039f1e&p1=5')