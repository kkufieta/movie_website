class Media():
    """
    Media class. Saves title, poster image and trailer urls for a media.
    """
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url


class Movie(Media):
    """
    Movie class. Saves title, poster image and trailer urls for a movie.
    """
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        Media.__init__(self, title, poster_image_url, trailer_youtube_url)


class TVSeries(Media):
    """
    TV Series class. Saves title, poster image and trailer urls
    for a TV series.
    """
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        Media.__init__(self, title, poster_image_url, trailer_youtube_url)
