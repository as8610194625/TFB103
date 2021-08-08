import requests
from bs4 import BeautifulSoup

landingPageUrl = "https://www.ptt.cc/ask/over18?from=%2Fbbs%2FGossiping%2Findex.html"
askOver18Url = "https://www.ptt.cc/ask/over18"
pttGossipUrl = "https://www.ptt.cc/bbs/Gossiping/index.html"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.62"}

ss = requests.session()
print(ss.cookies)
# Get form data
resLandingPageUrl = ss.get(landingPageUrl,headers=headers)
soupLanfingPageUrl = BeautifulSoup(resLandingPageUrl.text,"html.parser")
print(ss.cookies)

data = dict()
key1 = soupLanfingPageUrl.select('input')[0]['name']
value1 = soupLanfingPageUrl.select('input')[0]['value']
data[key1]=value1

key2 = soupLanfingPageUrl.select('button')[0]['name']
value2 = soupLanfingPageUrl.select('button')[0]['value']
data[key2]=value2
print(data)
ss.post(askOver18Url,headers=headers,data=data)
print(ss.cookies)
res = ss.get(pttGossipUrl,headers=headers)
print(res.text)