from collections import Counter
from pprint import pprint
from pymongo import MongoClient

client = MongoClient()

client = MongoClient('localhost', 27017)
db = client['twitter_db']

"""
# prints entire db 
cursor = db.tweet_collection.find({})
for item in cursor: 
    pprint(item)

"""
"""
# find users that have a specific keyword
search = "girl"
cursor = db.tweet_collection.find({"keyword": search})
print "Search Word:", search
for item in cursor:
    pprint(item["handle"])
"""


# Finds the 10 most popular keywords across all twitter handles

common_word = []

# adds each keyword to common_word (gets rid of ID tag)
for document in db.tweet_collection.find({}, {"keyword":1,"_id":0}):
    common_word += document["keyword"]

# set amount of keywords you want to find by changing number
common_word_count = Counter(common_word).most_common(10)
print common_word_count
print " "

# finds who is posting images about what

for x, y in common_word_count:
    if y > 1:
        print "Keyword:",x
        print "Count of word:",y
        print "Twitter Handles with Keyword: "
       
        cursor = db.tweet_collection.find({"keyword": x})
        for document in cursor:
            pprint(document["handle"])
        print " "



