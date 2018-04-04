import twitter
import datetime
import labelvideo

from pymongo import MongoClient

client = MongoClient()

handles = ['katyperry', 'justinbieber','BarackObama','rihanna','taylorswift13',
           'ladygaga', 'TheEllenShow', 'YouTube', 'Cristiano','jtimberlake',
           'twitter','KimKardashian','britneyspears','ArianaGrande','selenagomez',
           'ddlovato','cnnbrk','shakira','jimmyfallon','realDonaldTrump']

for i in range(0, 20):

    keywords = []

    twitter.downloadTweets(handles[i])
    keywords = labelvideo.labelVideo()
    num_image = len(keywords)

    # creates a db instance
    client = MongoClient('localhost', 27017)
    db = client['twitter_db']

    # posts to db 
    collection = db.tweet_collection

    data = {
        'handle': handles[i],
        'keyword': keywords,
        'num_images': num_image,
        'created': datetime.datetime.now()
    }
    
    result = collection.insert_one(data)
