import urllib.request
url = 'http://www.whatismyip.com.tw/'

'''
proxy_support = urllib.request.ProxyHandler({'http':'222.161.16.10:9999'})
openner = urllib.request.build_opener(proxy_support)
urllib.request.install_opener(openner)
respose = openner.open(url)
'''
respose = urllib.request.urlopen(url)
html = respose.read().decode('utf-8')
print(html)
