# EC500 Twitter API Project

This program will take a twitter handle, find the media files in the last 200 tweets and download them. It then stitches them together
using ffmpeg into a video. Finally, you will receive command line outputs and an output.txt file about what the video is generally about.

### Prerequisites
  Make sure all the proper packages are downloaded including:
  ```
  pip
  sudo easy_install pip
  ```
  ```
  homebrew
  /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
  ```
  ```
  wget
  brew install wget 
  ```
  ```
  tweepy
  google-cloud
  ffmpeg
  Pillow (PIL)
  ```
### Running instructions
  *Note: Set up Google Cloud credentials as a global variable*
  
  To use in program, insert a twitter handle and credentials.
