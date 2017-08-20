#!/usr/bin/env python
import urllib 
import re 
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
        reg = r'src="(.+?\.jpg)" pic_ext'
        imgre = re.compile(reg)
        imglist = re.findall(imgre,html)
        return imglist      
                   

#html = getHtml("http://pic.sogou.com/pics?query=%C3%C0%C5%AE&di=2&_asf=pic.sogou.com&w=05009900&sut=4529&sst0=1482586228795")
#html = getHtml("http://123.sogou.com/yule/meinv.html")
html = getHtml("http://pic.sogou.com/pics?query=%D7%C0%C3%E6&p=40230500&st=255&mode=255")
print html
