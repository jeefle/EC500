import twitter
import makevid
import labelvideo

username = 'realDonaldTrump'

twitter.downloadTweets(username, "guLZFthXS6Pdwut5nUnpGf6hk", "pN12roFkaX3CphLOvTquc14yPDBK9WJ7ePXPz4U3qZra96UH9D", "557327852-Zfm38pkBthBM2sotwRJp8pbbBQTQ2RaZg0tb1Zen", "Fl5N2FttpN4LDym09Ljg0bPWv8PrzvRoBqNsSgsYI6jBU")
makevid.convertToVideo(username)
labelvideo.labelVideo()