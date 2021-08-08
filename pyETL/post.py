import requests
from bs4 import BeautifulSoup

url = "https://web.pcc.gov.tw/tps/pss/tender.do?searchMode=common&searchType=advance"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.62"}

dataStr="""
method: sear
searchMethod: true
searchTarget: ATM
orgName: saasadasd
orgId: 
hid_1: 1
tenderName: sadasdsad
tenderId: 
tenderStatus: 5,6,20,28
tenderWay: 
awardAnnounceStartDate: 110/08/07
awardAnnounceEndDate: 110/08/07
proctrgCate: 
tenderRange: 
minBudget: 
maxBudget: 
item: 
hid_2: 1
gottenVendorName: 
gottenVendorId: 
hid_3: 1
submitVendorName: 
submitVendorId: 
location: 
execLocationArea: 
priorityCate: 
isReConstruct: 
btnQuery: 查詢"""
data = dict()
data = {i.split(': ')[0]: i.split(': ')[1] for i in dataStr.split('\n')}
res = requests.post(url,headers=headers,data=data)
soup = BeautifulSoup(res.text,"hrml.parser")
hiddenInputs = soup.select('div[id="print_area"] td[align="left"]') 
# print(res.text)
for hiddenInput in hiddenInputs:
