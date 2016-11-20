# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
						"A story about a boy and his toy",
						"http://www.gstatic.com/tv/thumb/movieposters/17420/p17420_p_v8_ab.jpg",
						"https://www.youtube.com/watch?v=KYz2wyBy3kc")
gladiator = media.Movie("Gladiator",
						"A story about revange of a Roman general",
						"https://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg",
						"https://www.youtube.com/watch?v=owK1qxDselE")

print "Name of this class: " + media.Movie.__name__
print "Name of Module including this class: " + media.Movie.__module__
# gladiator.show_trailer()
# toy_story.show_trailer()

# print(toy_story.storyline)

# avatar = media.Movie()



# movies = [toy_story, gladiator]
# fresh_tomatoes.open_movies_page(movies)
