import fresh_tomatoes
import media
# instancies of Movie class in media.py file 
toy_story = media.Movie("toy story",
                        "story of a boy and his toys that come to life",
                        "https://goo.gl/qWZoGk",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://goo.gl/GlK2Jn",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

the_matrix = media.Movie("the matrix",
                         "the other world the is controled by aliens",
                         "https://goo.gl/RIksxw",
                         "https://www.youtube.com/watch?v=vKQi3bBA1y8")

ratatouille = media.Movie("ratatouille",
                          "storyline",
                          "https://goo.gl/CA68kY",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("midnight in paris",
                                "storyline",
                                "https://goo.gl/NQ2qx4",
                                "https://www.youtube.com/watch?v=BYRWfS2s2v4")

hunger_games = media.Movie("hunger games",
                           "storyline",
                           "https://goo.gl/essTxY",
                           "https://www.youtube.com/watch?v=n-7K_OjsDCQ")
# an array of the favourite movies
movies = [toy_story, avatar, the_matrix, ratatouille,
          midnight_in_paris, hunger_games]
# open_movies_page methd is called from fresh_tomatoes.py file
fresh_tomatoes.open_movies_page(movies)
