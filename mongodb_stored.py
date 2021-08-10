from pymongo import MongoClient, collection
connection = MongoClient(host='localhost',port=27017)
db = connection.stock
collection = db['stock']
# print("collection:",collection)
import csv
with open("C:/Users/Tibame/Desktop/0050元大202106.csv",newline="",encoding='utf-8') as csvfile:
    rows = csv.reader(csvfile)
    for row in rows:
        # print(row[0], row[1])
        print("----------")
        each_row = {
        "_id":('').join(row[0].split('/')), 
        '成交股數': ('').join(row[1].split(',')),
        '成交金額':('').join(row[2].split(',')),
        '開盤價':row[3],
        '最高價':row[4],
        '最低價':row[5],
        '收盤價':row[6],
        '漲跌價差':row[7],
        '成交筆數':('').join(row[8].split(','))
        }
        try:
            result = collection.insert([each_row])
            print('已新增',each_row)
            print("----------")
        except:
            print('已存在_id',each_row['_id'],'(因此不寫入)')
            print("----------")



            


