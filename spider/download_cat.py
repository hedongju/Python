import urllib.request
req = urllib.request.Request('http://placekitten.com/g/500/500')
respose = urllib.request.urlopen(req)
cat_img = respose.read()

with open('cat_500_500.jpg','wb') as f:
    f.write(cat_img)
    f.close()
