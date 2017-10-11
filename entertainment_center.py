""" Defines the movies in the browser and instantiates the web browser. """

import fresh_tomatoes
import media

""" Movies defined here """

blade_runner = media.Movie("Blade Runner 2049", 
                           "https://i.pinimg.com/originals/a8/e9/0a/a8e90a844bed9e6951de16f5f6cde1e0.jpg",
						   "https://www.youtube.com/watch?v=gCcx85zbxz4")

zootopia = media.Movie("Zootopia",
                       "https://i.ytimg.com/vi/d4WEUn0yS74/movieposter.jpg",
					   "https://www.youtube.com/watch?v=jWM0ct-OLsM")

lalaland = media.Movie("La La Land",
                       "https://pics.filmaffinity.com/la_la_land-262021831-large.jpg",
					   "https://www.youtube.com/watch?v=0pdqf4P9MB8")

lego_movie = media.Movie("The Lego Movie",
                         "https://i.ytimg.com/vi/lVl6UxiDQQs/movieposter.jpg",
						 "https://www.youtube.com/watch?v=fZ_JOBCLF-I")

star_wars_vii = media.Movie("Star Wars: Episode VII - The Force Awakens",
                            "https://i.pinimg.com/originals/c9/69/72/c969723484d7cf353350e5fe3a5efc73.jpg",
							"https://www.youtube.com/watch?v=sGbxmsDFVnE")

finding_dory = media.Movie("Finding Dory",
                           "https://i.ytimg.com/vi/fqNhnLkg-7U/movieposter.jpg",
						   "https://www.youtube.com/watch?v=3JNLwlcPBPI")

"""
Stores the movies in a list called movies and call fresh_tomatoes.open_movies_page to display the movies
in a web browser
"""

movies = [blade_runner, zootopia, lalaland, lego_movie, star_wars_vii, finding_dory]
fresh_tomatoes.open_movies_page(movies)



