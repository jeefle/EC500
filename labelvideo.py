from google.cloud import vision
import io
import glob
import os

def labelVideo():
	#initiates client
	client = vision.ImageAnnotatorClient()
	labels_dict = {}
	#gets all the images in file
	path = glob.glob('*.jpg')

	count = 0

	#opens a file and instantiates a string
	file = open('output.txt', 'w')
	string = ""

	for img in path:
		with io.open(img, 'rb') as image_file:
			content = image_file.read()

		image = vision.types.Image(content=content)
		response = client.label_detection(image=image)
		labels = response.label_annotations

		labels_dict[count] = []

		x = 0

		for label in labels:
			if (x == 0):
				x = x + 1
				y = label.description
				print(y)
				string = string + y + '\n'
		count += 1

	file.write(string)
	file.close()

	#deletes old images in folder leaving only the movie and output.txt
	for oldimg in path:
		os.remove(oldimg)