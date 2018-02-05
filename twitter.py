#!/usr/bin/python

''' 
Jeffrey Leong

A script that downloads all the pictures posted by a given user and creates a video.
Adapted from Krishanu Konar.
'''

import json
from tweepy import OAuthHandler, API, Stream
from google.cloud import vision
import io, os
import wget
import sys
import requests
import glob


def main():
	#Authentication, enter keys
	CONSUMER_KEY = "INSERT YOUR OWN KEY"
	CONSUMER_SECRET = "INSERT YOUR OWN KEY"
	ACCESS_TOKEN = "INSERT YOUR OWN KEY"
	ACCESS_TOKEN_SECRET = "INSERT YOUR OWN KEY"

	auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
	api = API(auth)

	print '\nTwitter Image Downloader:\n========================'
	username = 'katyperry'
	max_tweets = 200
	
	all_tweets = getTweetsFromUser(username,max_tweets,api)
	media_URLs = getTweetMediaURL(all_tweets)
	
	downloadFiles(media_URLs,username)
	print '\n\nFinished Downloading.\n'
	changeFileName(username)
	convertToVideo()
	labelVideo()

def getTweetsFromUser(username,max_tweets,api):
	## Fetches Tweets from user with the handle 'username' upto max of 'max_tweets' tweets
	last_tweet_id, num_images = 0,0
	try:
	    raw_tweets = api.user_timeline(screen_name=username,include_rts=False,exclude_replies=True)
	except Exception as e:
		print e
		sys.exit()

	last_tweet_id = int(raw_tweets[-1].id-1)
	
	print '\nFetching tweets.....'

	if max_tweets == 0:
		max_tweets = 3500

	while len(raw_tweets)<max_tweets:
		sys.stdout.write("\rTweets fetched: %d" % len(raw_tweets))
		sys.stdout.flush()
		temp_raw_tweets = api.user_timeline(screen_name=username, max_id=last_tweet_id, include_rts=False, exclude_replies=True)

		if len(temp_raw_tweets) == 0:
			break
		else:
			last_tweet_id = int(temp_raw_tweets[-1].id-1)
			raw_tweets = raw_tweets + temp_raw_tweets

	print '\nFinished fetching ' + str(min(len(raw_tweets),max_tweets)) + ' Tweets.'
	return raw_tweets

def getTweetMediaURL(all_tweets):
	print '\nCollecting Media URLs.....'
	tweets_with_media = set()
	for tweet in all_tweets:
		media = tweet.entities.get('media',[])
		if (len(media)>0):
			tweets_with_media.add(media[0]['media_url'])
			sys.stdout.write("\rMedia Links fetched: %d" % len(tweets_with_media))
			sys.stdout.flush()
	print '\nFinished fetching ' + str(len(tweets_with_media)) + ' Links.'

	return tweets_with_media

#creates new folder and downloads
def downloadFiles(media_url,username):
	print '\nDownloading Images.....'
	try:
	    os.mkdir('twitter_images')
	    os.chdir('twitter_images')
	except:
		os.chdir('twitter_images')

	try:
	    os.mkdir(username)
	    os.chdir(username)
	except:
		os.chdir(username)

	for url in media_url:
		wget.download(url)

#changes file names of downloaded in order to easily concatenate using ffmpeg		
def changeFileName(username):
	os.system('j=1; for i in *.jpg; do mv "$i" file"$j".jpg; let j=j+1;done')
	print 'file names changed'

#concatenates pictures into a video
def convertToVideo():
	os.system("ffmpeg -framerate .5 -pattern_type glob -i '*.jpg' out.mp4")
	print 'video created'

def labelVideo():
	labels_dict = {}
	path = glob.glob('*.jpg')
	client = vision.ImageAnnotatorClient()
	count = 0

	for img in path:
		with io.open(img, 'rb') as image_file:
			content = image_file.read()

		image = vision.types.Image(content=content)
		response = client.label_detection(image=image)
		labels = response.label_annotations
		labels_dict[count] = []

		for label in labels:
			labels_dict[count].append(label.description)
		count += 1

	print(labels_dict)

if __name__ == '__main__':
	main()
