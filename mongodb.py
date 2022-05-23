import pymongo
client=pymongo.MongoClient()

db=client["mydb"]
mycol=db["user"]

datalist=[{'username':"", 'password':""}, {'username':"", 'password':""}]
db.collection.insert_many(datalist)

print(db.inserted_ids)
#reference
#for x in mycol.find({"_id":1, "password":1}):
 #   print(x)