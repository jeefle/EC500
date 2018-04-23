import json
import pymongo
 
from pymongo import MongoClient
client = MongoClient()
 
db = client.airports
collection = db.airpot_collection
page = open("airports.json",'r')
dataset = json.loads(page.read())


# inserts db

for item in dataset:
 collection.insert(item)

# prints entire db
for item in collection.find():
 print(item)
print("\n") 

#prints specific airport with ID
print("Document with id = JFK")
for item in collection.find({"code": "ATL"}):
 print(item)
print("\n")
