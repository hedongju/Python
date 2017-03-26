#! /usr/bin/python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright 漏 2017 hedj <hedj@hedj-virtual-machine>
#
# Distributed under terms of the MIT license.

"""

"""
import requests
from bs4 import BeautifulSoup

res = requests.get('http://fangchan.news.baidu.com')
#res.encoding  = 'utf-8' ###用自己指定的utf-8编码格式解析原来站点真实的编码格式，如果原来站点的编码格式不是utf-8，则就会出现乱码
###解决乱码问题：
#print(res.apparen_encoding) ###获得原站点的真实编码格式（GB2312）,指定用GB2312格式去解析原站点的数据
res.encoding = 'GB2312'
soup = BeautifulSoup(res.text,'html.parser')
for news in soup.select('.tlc-fl'):
    h2 = (news.select('a')[0].text)
    myhref = news.select('a')[0]['href']
#   print(h2,myhref) #打印有问题 
    print(h2)
    print(myhref)
#print(res.text)

