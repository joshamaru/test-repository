import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
pos = input ('Position:')
pos = int(pos)
iter = input ('Number of times:')
iter = int(iter)
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('a')
count = 1
nurl = dict()
key = 1
for tag in tags:
    nurl[key] = tag.get('href', None)
    key = key +1
print (nurl[pos])
while count < iter:
    url = nurl[pos]
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    nurl = dict()
    key = 1
    count = count + 1
    for tag in tags:
        nurl[key] = tag.get('href', None)
        key = key +1
    print (nurl[pos])
namein = nurl[pos].find("by_") + 3
print(nurl[pos][namein:-5])
