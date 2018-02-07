import glob
import os

#changes file names of downloaded in order to easily concatenate using ffmpeg		
def convertToVideo(username):
	#removes previous video
	path = glob.glob('*.mp4')
	for vid in path:
		os.remove(vid)

	os.system('j=1; for i in *.jpg; do mv "$i" file"$j".jpg; let j=j+1;done')
	print 'File names changed \n'
	#converts to video
	os.system("ffmpeg -framerate .5 -pattern_type glob -i '*.jpg' out.mp4")
	print 'Video created \n'

