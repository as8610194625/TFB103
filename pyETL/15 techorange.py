import requests
import json
from bs4 import BeautifulSoup

url = "https://buzzorange.com/techorange/wp/wp-admin/admin-ajax.php"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.62"}
dataStr = """action: ceris_posts_listing_grid_b_no_sidebar
args[post_type]: post
args[ignore_sticky_posts]: 1
args[post_status]: publish
args[posts_per_page]: 6
args[offset]: 0
args[orderby]: date
postOffset: 6
type: loadmore
moduleInfo[post_source]: all
moduleInfo[post_icon]: disable
moduleInfo[iconPosition]: top-right
moduleInfo[post_icon_animation]: disable
moduleInfo[bookmark]: off
securityCheck: ab248723a6"""
data = {r.split(': ')[0]:r.split(': ')[1] for r in dataStr.split('\n')}
for i in range(0,3):
    # print(data)
    res = requests.post(url,headers=headers,data=data)
    # print(res.text)
    jsonData = json.loads(res.text)
    # print(jsonData) #回傳str 型別像html 可帶入Beautyfulsoup
    soup = BeautifulSoup(jsonData,"html.parser")
    titles = soup.select('h3[class="post__title typescale-2"] a')#select 用法 取標籤中的標籤 多一個space
    for title in titles:
        titleName = title.text
        titleUrl = title['href']
        print(titleName)
        print(titleUrl)
        print("==========")

    data['postOffset'] = str(int(data['postOffset']) + 6)
    print('+++++++++++++++++++')