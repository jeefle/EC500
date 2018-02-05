#!/usr/bin/python

''' 
Jeffrey Leong

A script that downloads all the pictures posted by a given user and creates a video.
Adapted from Krishanu Konar.
'''

import json
from tweepy import OAuthHandler, API, Stream
import os
import wget
import sys
import requests


def main():
	#Authentication, enter keys
	CONSUMER_KEY = "guLZFthXS6Pdwut5nUnpGf6hk"
	CONSUMER_SECRET = "pN12roFkaX3CphLOvTquc14yPDBK9WJ7ePXPz4U3qZra96UH9D"
	ACCESS_TOKEN = "557327852-Zfm38pkBthBM2sotwRJp8pbbBQTQ2RaZg0tb1Zen"
	ACCESS_TOKEN_SECRET = "Fl5N2FttpN4LDym09Ljg0bPWv8PrzvRoBqNsSgsYI6jBU"

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

if __name__ == '__main__':
	main()