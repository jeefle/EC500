import twitter
import makevid
import labelvideo

def downloadconvert(username, "CONSUMER_KEY", "CONSUMER_SECRET", "ACCESS_TOKEN", "ACCESS_TOKEN_KEY")
	twitter.downloadTweets(username, "CONSUMER_KEY", "CONSUMER_SECRET", "ACCESS_TOKEN", "ACCESS_TOKEN_KEY")
	makevid.convertToVideo(username)
	labelvideo.labelVideo()
