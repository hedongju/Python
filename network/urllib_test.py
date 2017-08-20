#!/usr/bin/env python
from urllib import urlopen
webpage = urlopen('http://www.cnblogs.com/IPrograming/')
txt = webpage.readline(45)
print txt
