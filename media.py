""" 
Defines the Movie class that is used to create instances of a movie to be displayed in the webbrowser 

"""

class Movie(object):
	""" 
	This class contains information about a movie such as title, poster url and youtube trailer 
	url.

	Attributes: 
	    movie_title: string containing title of the movie
	    poster_image_url: string containing url to the movie poster
	    trailer_youtube_url: string containing url to movie trailer in youtube
	"""

	def __init__(self, movie_title, poster_image_url, trailer_youtube_url):
		""" Inits Movie class with movie title, image and youtube trailer urls """
		self.title = movie_title
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url

