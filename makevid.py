import glob
import os
from PIL import Image
	
def convertToVideo(username):
	#removes previous video
	pathVid = glob.glob('*.mp4')
	for vid in pathVid:
		os.remove(vid)

	# renames images
	os.system('j=1; for i in *.jpg; do mv "$i" file"$j".jpg; let j=j+1;done')
	print 'File names changed \n'

	# resizes images to 750 x 750 (new files named resized)
	path = glob.glob('*.jpg')
	for img in path:
		im = Image.open(img)
		im = im.resize((750, 750))
		out_file_name = os.path.join('resize' + img)
		im.save(out_file_name)
	print 'Images resized \n'

	# removes old images
	path = glob.glob('file?.jpg')
	for oldimg in path:
		os.remove(oldimg)

	#converts to video
	os.system("ffmpeg -framerate .5 -pattern_type glob -i '*.jpg' out.mp4")
	print 'Video created \n'
