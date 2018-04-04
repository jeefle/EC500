from google.cloud import vision
import io
import glob
import os

def labelVideo():
	#initiates client
	client = vision.ImageAnnotatorClient()
	#gets all the images in file
	path = glob.glob('*.jpg')

	count = 0
	z =[]

	#opens a file and instantiates a string
	string = ""

	for img in path:
		with io.open(img, 'rb') as image_file:
			content = image_file.read()

		image = vision.types.Image(content=content)
		response = client.label_detection(image=image)
		labels = response.label_annotations

		x = 0

		# prints the first label aka the most relevent label
		for label in labels:
			if (x == 0):
				y = label.description
				z.append(y)
				x = x + 1
	
	#deletes old images in folder leaving only the movie and output.txt
	for oldimg in path:
		os.remove(oldimg)

	return z

	


	