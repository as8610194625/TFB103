import requests


url = "https://www.ptt.cc/bbs/Gossiping/index.html"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.62"}

cookies = {'over18':'1'}

res = requests.get(url,headers=headers,cookies=cookies)
print(res.text)