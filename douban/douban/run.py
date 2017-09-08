#!/usr/bin/env python
#-*- coding: utf-8 -*-

from scrapy import cmdline

name='douban'
cmd='scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())