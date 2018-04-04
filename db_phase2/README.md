# Database Analysis with Twitter
This saves the data gathered from the original twitter project and saves to MongoDB database

## Getting Started
Download each file. Be sure to edit password.py for your own twitter keys. Also be sure to set the global variable for google cloud vision using
```
export GOOGLE_APPLICATION_CREDENTIALS=PATH_TO_KEY_FILE
```
### Prerequisites
- MongoDB
- pymongo 
- python 3

### Database Structure
This program takes the last 50 tweets in a twitter feed, finds the images and then generates keywords to describe the image.

The database is structured as seen below with fields for handle (user input), keyword, number of images in a feed, and logs of when the data was inserted.
```
{
 u'_id': ObjectId('5ac4ebf962bb6c755245cc3e'),
 u'time': datetime.datetime(2018, 4, 4, 11, 15, 5, 240000),
 u'handle': u'BarackObama',
 u'keyword': [u'social group',
              u'window',
              u'event',
              u'social group',
              u'black',
              u'recreation',
              u'profession',
              u'vacation'],
 u'num_images': 8}
```

### Analytics
Seen in the statistics.py file, the code has three functions.
1. Print the entire database 
1. Given a specific word, find who has been posting images of it
1. Aggregate all keywords, find the top 10 most used, and the twitter handles of those who posted images of the keyword.
