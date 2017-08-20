import urllib.request
import urllib.parse

url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom='
data = {}
data['i'] = 'i love you'
data['from'] = 'AUTO'
data['to'] = 'AUTO'
data['smartresult'] = 'dict'
data['client'] = 'fanyideskweb'
data['salt'] = '1503202042336'
data['sign'] = '0854c4159be41d341e6252653b81c50d'
data['doctype'] = 'json'
data['version'] = '2.1'
data['keyfrom'] = 'fanyi.web'
data['action'] = 'FY_BY_CLICKBUTTION'
data['typoResult'] = 'true'
data = urllib.parse.urlencode(data).encode('UTF-8')

respose = urllib.request.urlopen(url,data)
html = respose.read().decode('utf-8')
print(html)
