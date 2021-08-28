import pymongo
import json

db = pymongo.MongoClient().tfb103

rows = db.lookupPerson.aggregate([
    {
      "$lookup":
        {
          "from": "lookupTel",
          "localField": "tel_group",
          "foreignField": "group",
          "as": "tel_arr"
        }
    }
    ,
    {"$sort":{"name":1}}
    ,
    {
      "$project":{
        "user":"$name",
        "tels":"$tel_arr",
        "_id":0
      }
    }
    ,
    {
      "$project":{
        "tels._id":0,
        "tels.group":0
      }
    }
])

for row in rows:
  print(json.dumps(row, indent=4))

