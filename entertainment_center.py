# to import media.py file
import media
# to import fresh_tomatoes.py
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A cowboy doll is profoundly threatened and"
                        " jealous when a new spaceman figure supplants him as top toy in a boy's room.",
                        "https://m.media-amazon.com/images/M/MV5BMDU2ZWJlMjktMTRhMy"
                        "00ZTA5LWEzNDgtYmNmZTEwZTViZWJkXkEyXkFqcGdeQXVyNDQ2OTk4MzI@._V1_UX182_CR0,0,182,268_AL_.jpg",
                        "https://youtu.be/KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A paraplegic marine dispatched to the moon Pandora on a unique mission becomes torn between"
                     " following his orders and protecting the world he feels is his home.",
                     "https://m.media-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@."
                     "_V1_UX182_CR0,0,182,268_AL_.jpg",
                     "https://youtu.be/5PSNL1qE6VY")

inception = media.Movie("Inception", "Inception is a movie starring Leonardo DiCaprio, Joseph Gordon-Levitt, and Ellen"
                                     " Page. A thief, who steals corporate secrets through the use of dream-sharing"
                                     " technology, is given the inverse task of planting an idea into the mind"
                                     " of a CEO.", "https://m.media-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnX"
                                                   "kFtZTcwNTI5OTM0Mw@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                        "https://www.youtube.com/watch?v=d3A3-zSOBT4")

avengers = media.Movie("Avengers", "Earth's mightiest heroes must come together and learn to fight as a team if"
                                   " they are going to stop the mischievous Loki and his alien army"
                                   " from enslaving humanity.",
                       "https://m.media-amazon.com/images/M/MV5BNDYxNjQyMjAtNTdiOS00NGYwLWFmNTAtNThmYjU5ZGI2YTI1"
                       "XkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UX182_CR0,0,182,268_AL_.jpg",
                       "https://www.youtube.com/watch?v=eOrNdBpGMv8")

death_note = media.Movie("Death Note", "Death Note is a movie starring Nat Wolff, Lakeith Stanfield, and"
                                       " Margaret Qualley. A high school student named Light Turner"
                                       " discovers a mysterious notebook that has the power to kill anyone"
                                       " whose name is written within its pages, and launches a secret crusade to rid"
                                       " the world of criminals.",
                         "https://m.media-amazon.com/images/M/MV5BMTUwOTgzMTEyOF5BMl5BanBnXkFtZTgwNTk3MTM5MjI@."
                                       "_V1_UX182_CR0,0,182,268_AL_.jpg",
                         "https://www.youtube.com/watch?v=0SiyGOyAlW4")

thor = media.Movie("Thor", "The powerful, but arrogant god Thor, is cast out of Asgard to live amongst humans in"
                           " Midgard (Earth), where he soon becomes one of their finest defenders.",
                   "https://m.media-amazon.com/images/M/MV5BOGE4NzU1YTAtNzA3Mi00ZTA2LTg2YmYtMDJmMThiMjlkYjg2Xk"
                   "EyXkFqcGdeQXVyNTgzMDMzMTg@._V1_UX182_CR0,0,182,268_AL_.jpg",
                   "https://www.youtube.com/watch?v=JOddp-nlNvQ")

movies = [toy_story, avatar, inception, avengers, death_note, thor]
fresh_tomatoes.open_movies_page(movies)
