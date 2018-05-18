import webbrowser


class Movie():

	"""This class provides a way to store movie related information"""
	
	VALID_RATINGS = ["G", "PG", "PG-13", "R"]
	
	# intialize function that takes in a title, storyline, poster URL, and trailer URL
	def __init__(self, mtitle, mstory, mposter, mtrailer):
		self.title = mtitle
		self.storyline = mstory
		self.poster_image_url = mposter
		self.trailer_youtube_url = mtrailer
		
	# this function opens a webpage displaying a youtube video
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)
		