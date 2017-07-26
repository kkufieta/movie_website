import media
import fresh_tomatoes

# Movies
bridget_diary = media.Movie("Bridget Jones's Diary", 
        "https://upload.wikimedia.org/wikipedia/en/1/17/BridgetJonesDiaryMoviePoster.jpg",
        "https://www.youtube.com/watch?v=DQdy98B1nf0")
bridget_edge = media.Movie("Bridget Jones: The Edge of Reason",
        "https://upload.wikimedia.org/wikipedia/en/7/7c/Bridget_jones_edge_of_reason_poster.jpg",
        "https://www.youtube.com/watch?v=2DFQNPx5sxA")
bridget_baby = media.Movie("Bridget Jones's Baby",
        "https://upload.wikimedia.org/wikipedia/en/e/e6/Bridget_Jones%27s_Baby_poster.jpg",
        "https://www.youtube.com/watch?v=mJsvmscPY9w")

# TV Series
unbreakable_kimmy = media.TVSeries("Unbreakable Kimmy Schmidt",
        "https://images-na.ssl-images-amazon.com/images/M/MV5BMjI4NjA2MDM4NF5BMl5BanBnXkFtZTgwODYxNDYwMjI@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
        "https://www.youtube.com/watch?v=mNKEKlXY3Z4")

jane_the_virgin = media.TVSeries("Jane The Virgin",
        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTQ1NDE5MTY5OV5BMl5BanBnXkFtZTgwNDA3Mzg5NjE@._V1_.jpg",
        "https://www.youtube.com/watch?v=0NTmJjtDYn0")

crazy_ex_girlfriend = media.TVSeries("Crazy Ex Girlfriend",
        "https://images-na.ssl-images-amazon.com/images/M/MV5BMzU3ODQxMjgzOV5BMl5BanBnXkFtZTgwNDg4NDgzMDI@._V1_.jpg",
        "https://www.youtube.com/watch?v=UK1Tj07c_co")


# Movie list
movies = [unbreakable_kimmy, jane_the_virgin, crazy_ex_girlfriend,
        bridget_diary, bridget_edge, bridget_baby]

# Create and open movie website
fresh_tomatoes.open_movies_page(movies)
