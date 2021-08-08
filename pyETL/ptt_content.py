import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/movie/index.html"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.62"}

articleUrl = "https://www.ptt.cc/bbs/movie/M.1628251622.A.0D8.html"
resArticle = requests.get(articleUrl,headers=headers)
soupArticle = BeautifulSoup(resArticle.text,"html.parser")
articleContent = soupArticle.select('div[id="main-content"]')[0]
# for i in articleContent.select('div'):
#     print(i)
#     print("==========")
# print("@@@@@@@@@@@@@@@@@@@@@@@@@@@")
# articleContent.select('div')[0].extract()  #return Tag and remove this Tag Object
for i in articleContent.select('div'):
    print(i.extract())
    print("==========")
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@")
for i in articleContent.select('span'):
    print(i.extract())
    print("==========")
print(articleContent.text)
