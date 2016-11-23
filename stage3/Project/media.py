# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define the class Movie. You could do this
# directly in entertainment_center.py but many developers keep their
# class definitions separate from the rest of their code. This also
# gives you practice importing Python files.

import webbrowser


class Video():
	"""Class of Video, include common attributes of videos
	 like title, poster image, trailer, director, and staring ..."""
	def __init__(self, title, poster_image_url, trailer_youtube_url, 
				director, screen_writer, stars):
		self.title = title
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url
		self.director = director
		self.screen_writer = screen_writer
		self.stars = stars


class Movie(Video):
    """This class provides a way to store movie related information.
	  And it inheritence several attributes from parent class Video"""
    def __init__(self, movie_title, poster_image_url, trailer_youtube_url,
    			director, screen_writer, stars, length, release_date):
    	Video.__init__(self, movie_title, poster_image_url, trailer_youtube_url, 
				director, screen_writer, stars)
        self.length = length
        self.release_date = release_date


# class Drama(Video):
# 	"""Drama class store drama informations. And it inheritance several 
# 		variables from parent class Video."""
# 	def __init__(self, drama_title,poster_image_url, trailer_youtube_url, 
#                 director, screen_writer, stars, seasons, episodes_of_season, episode_length):
# 	    Video.__init__(self, drama_title, poster_image_url, trailer_youtube_url, 
# 				director, screen_writer, stars)
# 	    self.seasons = seasons
#         self.episodes_of_season = episodes_of_season
#         self.episode_length = episode_length