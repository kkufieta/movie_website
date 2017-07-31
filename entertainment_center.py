import media
import fresh_tomatoes

# Movies Poster Image URLs
bridget_diary_img_url = "https://upload.wikimedia.org/wikipedia/en/1/17/BridgetJonesDiaryMoviePoster.jpg"  # noqa
bridget_edge_img_url = "https://upload.wikimedia.org/wikipedia/en/7/7c/Bridget_jones_edge_of_reason_poster.jpg"  # noqa
bridget_baby_img_url = "https://upload.wikimedia.org/wikipedia/en/e/e6/Bridget_Jones%27s_Baby_poster.jpg"  # noqa

# Movies Trailer URLs
bridget_diary_video_url = "https://www.youtube.com/watch?v=DQdy98B1nf0"  # noqa
bridget_edge_video_url = "https://www.youtube.com/watch?v=2DFQNPx5sxA"  # noqa
bridget_baby_video_url = "https://www.youtube.com/watch?v=mJsvmscPY9w"  # noqa

# TV Series Poster Image URLs
unbreakable_kimmy_img_url = "https://images-na.ssl-images-amazon.com/images/M/MV5BMjI4NjA2MDM4NF5BMl5BanBnXkFtZTgwODYxNDYwMjI@._V1_SY1000_CR0,0,674,1000_AL_.jpg"  # noqa
jane_the_virgin_img_url = "https://images-na.ssl-images-amazon.com/images/M/MV5BMTQ1NDE5MTY5OV5BMl5BanBnXkFtZTgwNDA3Mzg5NjE@._V1_.jpg"  # noqa
crazy_ex_girlfriend_img_url = "https://images-na.ssl-images-amazon.com/images/M/MV5BMzU3ODQxMjgzOV5BMl5BanBnXkFtZTgwNDg4NDgzMDI@._V1_.jpg"  # noqa

# TV Series Trailer URLs
unbreakable_kimmy_video_url = "https://www.youtube.com/watch?v=mNKEKlXY3Z4"  # noqa
jane_the_virgin_video_url = "https://www.youtube.com/watch?v=0NTmJjtDYn0"  # noqa
crazy_ex_girlfriend_video_url = "https://www.youtube.com/watch?v=UK1Tj07c_co"  # noqa

# Movies
bridget_diary = media.Movie("Bridget Jones's Diary",
                            bridget_diary_img_url,
                            bridget_diary_video_url)

bridget_edge = media.Movie("Bridget Jones: The Edge of Reason",
                           bridget_edge_img_url,
                           bridget_edge_video_url)

bridget_baby = media.Movie("Bridget Jones's Baby",
                           bridget_baby_img_url,
                           bridget_baby_video_url)

# TV Series
unbreakable_kimmy = media.TVSeries("Unbreakable Kimmy Schmidt",
                                   unbreakable_kimmy_img_url,
                                   unbreakable_kimmy_video_url)

jane_the_virgin = media.TVSeries("Jane The Virgin",
                                 jane_the_virgin_img_url,
                                 jane_the_virgin_video_url)

crazy_ex_girlfriend = media.TVSeries("Crazy Ex Girlfriend",
                                     crazy_ex_girlfriend_img_url,
                                     crazy_ex_girlfriend_video_url)


# Movie list
movies = [unbreakable_kimmy,
          jane_the_virgin,
          crazy_ex_girlfriend,
          bridget_diary,
          bridget_edge,
          bridget_baby]

# Create and open movie website
fresh_tomatoes.open_movies_page(movies)
