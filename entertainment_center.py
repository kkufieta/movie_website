import media
import fresh_tomatoes

bridget_diary = media.Movie("Bridget Jones's Diary", 
        "https://upload.wikimedia.org/wikipedia/en/1/17/BridgetJonesDiaryMoviePoster.jpg",
        "https://www.youtube.com/watch?v=DQdy98B1nf0")
bridget_edge = media.Movie("Bridget Jones: The Edge of Reason",
        "https://upload.wikimedia.org/wikipedia/en/7/7c/Bridget_jones_edge_of_reason_poster.jpg",
        "https://www.youtube.com/watch?v=2DFQNPx5sxA")
bridget_baby = media.Movie("Bridget Jones's Baby",
        "https://upload.wikimedia.org/wikipedia/en/e/e6/Bridget_Jones%27s_Baby_poster.jpg",
        "https://www.youtube.com/watch?v=mJsvmscPY9w")

movies = [bridget_diary, bridget_edge, bridget_baby]
fresh_tomatoes.open_movies_page(movies)
