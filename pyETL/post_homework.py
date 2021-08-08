import requests
from bs4 import BeautifulSoup



url = "http://ec2-13-114-140-26.ap-northeast-1.compute.amazonaws.com/practice/tfb103"
purl = "http://ec2-13-114-140-26.ap-northeast-1.compute.amazonaws.com/practice/tfb103"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.62"}
# headersring ="""Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
# Accept-Encoding: gzip, deflate
# Accept-Language: zh-TW,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
# Cache-Control: max-age=0
# Connection: keep-alive
# Content-Length: 30
# Content-Type: application/x-www-form-urlencoded
# Host: ec2-13-114-140-26.ap-northeast-1.compute.amazonaws.com
# Origin: http://ec2-13-114-140-26.ap-northeast-1.compute.amazonaws.com
# Referer: http://ec2-13-114-140-26.ap-northeast-1.compute.amazonaws.com/practice/tfb103
# Upgrade-Insecure-Requests: 1
# User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67"""
# headers = {}
# for row in headersring.split('\n'):
#     headers[row.split(': ')[0]] = row.split(': ')[1]
ss = requests.session()
print(ss.cookies)
ssres = ss.get(url,headers=headers)
ssoup = BeautifulSoup(ssres.text,"html.parser")
print(ss.cookies)
data = dict()
key1 = ssoup.select('input')[0]['name']
value1 = 'Ni'
data[key1] = value1
key2 = ssoup.select('input')[1]['name']
value2 = ssoup.select('input')[1]['value']
data[key2] = value2
key3 = ssoup.select('input')[2]['type']
value3 = ssoup.select('input')[2]['value']
data[key3] = value3
res = ss.post(url,headers=headers,data=data)
print(data)
print(ss.cookies)
print(res.text)