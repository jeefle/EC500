from flask import Flask
#from testtwitter2 import get_all_tweets
import twitter


app = Flask(__name__)


@app.route("/")
def main():
	return """
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset = "UTF-8">
	<title>Title</title>
</head>
	<h1> EC500 API Assignment 2 </h1>
	<p1> by Jeffrey Leong </p1>
<br>
<br>
<video width:700px;height:700px;" width="700" height="700" controls>
  <source src="out.mp4" type="video/mp4">
Your browser does not support the video tag.
</video>
	</body>
</html>
	"""


if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)
