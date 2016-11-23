# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

import media
import fresh_tomatoes

	
the_shawshank_redemption = media.Movie("The Shawshank Redemption",
							"https://img3.doubanio.com/view/photo/photo/public/p480747492.jpg",
							"https://www.youtube.com/watch?v=6hB3S9bIaco",
							"Frank Darabont",
							"Frank Darabont, Stephen King",
							"Tim Robbins, Morgan Freeman",
							"142 min",
							"1994-10-14")

life_is_beautiful = media.Movie("La vita e bella",
							"https://img3.doubanio.com/view/photo/photo/public/p2194576972.jpg",
							"https://www.youtube.com/watch?v=pysuUJhOnv4",
							"Roberto Benigni",
							"Roberto Benigni, Vincenzo Cerami",
							"Roberto Benigni, Nicoletta Braschi, VGiorgio Cantarini",
							"116 min",
							"1997-12-20")

farewell_my_concubine = media.Movie("Farewell My Concubine",
							"https://img1.doubanio.com/view/photo/photo/public/p2390676609.jpg",
							"https://www.youtube.com/watch?v=6qvMdtFmcjQ",
							"Kaige Chen",
							"Wei Lu, Lilian Lee Pik-Wah",
							"Leslie Cheung, Fengyi Zhang, Li Gong",
							"171 min",
							"1993-01-01")	

movies = [the_shawshank_redemption, life_is_beautiful, farewell_my_concubine]
fresh_tomatoes.open_movies_page(movies)
