from urllib import request
import requests
import json
import os

if not os.path.exists('C:/Users/Tibame/Desktop/pyETL/dcard_photos'):
    os.mkdir('C:/Users/Tibame/Desktop/pyETL/dcard_photos')


url = "https://www.dcard.tw/service/api/v2/forums/photography/posts?limit=30&before=236646571"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.62"}

res = requests.get(url,headers=headers)
# print(res.text)
## id ->url
## article -> article
## title -> title 
## mediaMeta -> images
jsonData = json.loads(res.text) # return list/dict
# for i in jsonData:
#     print(i)
# print(jsonData[0].keys())
# for k in jsonData[0]:
#     print(k)
for articleDict in jsonData:
    title = articleDict['title']
    articleUrl = "https://www.dcard.tw/f/photography/p/" + str(articleDict['id'])
    print(title)
    print(articleUrl)
    for imgs in articleDict['mediaMeta']:
        print('\t'+imgs['url'])
        # imagePath = 'C:/Users/Tibame/Desktop/pyETL/dcard_photos/{}.{}'.format(title,imgs['url'].split('.')[-1])
        imagePath = 'C:/Users/Tibame/Desktop/pyETL/dcard_photos/{}_{}'.format(title,imgs['url'].split('/')[-1])
        # request.urlretrieve(imgs['url'],imagePath) #urllib 寫法
        imgContent = requests.get(imgs['url'],headers=headers).content #requests寫法
        with open(imagePath,'wb') as f:#requests寫法
            f.write(imgContent)#requests寫法
    print("============================")
