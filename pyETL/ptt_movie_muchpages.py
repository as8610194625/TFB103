import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/movie/index%s.html"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.62"}

page = 9508

for i in range(0,5):
    res = requests.get(url%(page),headers=headers)
    soup = BeautifulSoup(res.text,"html.parser")
    titles = soup.select('div[class="title"]')

    # for titleSoup in titles:
    #     try:
    #         title = titleSoup.select('a')[0].text #如果出現IndexError，代表此list為空
    #         articleURL = "https://www.ptt.cc"+titleSoup.select('a')[0]['href']
    #         print(articleURL)
    #         print(title)
    #     except IndexError:
    #         print(titleSoup)
    #     print("============================")
    for titleSoup in titles:
        if titleSoup.select('a').__len__() == 0:
            continue
        title = titleSoup.select('a')[0].text #如果出現IndexError，代表此list為空
        articleURL = "https://www.ptt.cc"+titleSoup.select('a')[0]['href']
        print(articleURL)
        print(title)
    
        print("============================")

    page -= 1