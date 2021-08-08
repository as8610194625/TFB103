import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/movie/index.html"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.62"}

res = requests.get(url,headers=headers)
# print(res.text,"html.parser")
soup = BeautifulSoup(res.text,"html.parser")
# print(soup)
# titles = soup.select('a') #return List
titles = soup.select('div[class="title"]')
for titleSoup in titles:
    title = titleSoup.select('a')[0].text
    articleURL = "https://www.ptt.cc"+titleSoup.select('a')[0]['href']
    print(articleURL)
    print(title)
    print("============================")