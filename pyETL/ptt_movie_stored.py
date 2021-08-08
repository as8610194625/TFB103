import requests
from bs4 import BeautifulSoup
import os


if not os.path.exists('C:/Users/Tibame/Desktop/pyETL/pttMovie'):
    os.mkdir('C:/Users/Tibame/Desktop/pyETL/pttMovie') 
url = "https://www.ptt.cc/bbs/movie/index.html"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.62"}



for i in range(0,5):
    res = requests.get(url,headers=headers)
    soup = BeautifulSoup(res.text,"html.parser")
    titles = soup.select('div[class="title"]')

    for titleSoup in titles:
        if titleSoup.select('a').__len__() == 0:
            continue
        title = titleSoup.select('a')[0].text #如果出現IndexError，代表此list為空
        articleURL = "https://www.ptt.cc"+titleSoup.select('a')[0]['href']
        #  Get article content↓ 
        resArticle = requests.get(articleURL,headers=headers)
        soupArticle = BeautifulSoup(resArticle.text,"html.parser")
        # articleContent = soupArticle.select('div[id="main-content"]')[0].text.split('※ 發信站')[0]
        # ↑　or ↓ 取出內容
        articleContentSoup = soupArticle.select('div[id="main-content"]')[0]
        # for i in articleContentSoup.select('div'):
        #     i.extract()
        # for i in articleContentSoup.select('span'):
        #     i.extract()
        # ↑　↓ 同一邏輯
        for tag in ['div','span']:
            i.extract()
        articleContent = articleContentSoup.text
        print(articleURL)
        print(title)
        try:
            with open('C:/Users/Tibame/Desktop/pyETL/pttMovie/{}.txt'.format(title),'w',encoding='utf-8') as f:
                f.write(articleContent)
        except FileNotFoundError:
            title = title.replace('/','_')
            with open('C:/Users/Tibame/Desktop/pyETL/pttMovie/{}.txt'.format(title),'w',encoding='utf-8') as f:
                f.write(articleContent)
        except OSError:
            pass
        print("============================")

    # GET NEW URL
    newURL = "https://www.ptt.cc"+soup.select('a[class="btn wide"]')[1]['href']
    url = newURL


