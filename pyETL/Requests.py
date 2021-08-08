import requests
from bs4 import BeautifulSoup


url = "https://www.ptt.cc/bbs/joke/index.html"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.62"}
res = requests.get(url,headers=headers)
html = res.text
soup = BeautifulSoup(html,"html.parser")
# print(soup)

# logo = soup.findAll('a',{'id':'logo'}) #findAll回傳一個List
# logo = soup.findAll('a',id = 'logo')
# logo = soup.select('a',id='logo')
# logo = soup.select('a[id="logo"]')
# findALL = select , Return 'List' !!!
logo = soup.select('a#logo')

print(logo[0])
print(logo[0].text)
print("https://www.ptt.cc"+logo[0]['href'])

content = soup.findAll('div',class_='bbs-content')
print(content[0])

board = content[0].findAll('a',class_='board')
print(board[0])
