class Media():
    """
    Media class
    """
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url


class Movie(Media):
    """
    Movie class
    """
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        Media.__init__(self, title, poster_image_url, trailer_youtube_url)


class TVSeries(Media):
    """
    TV series class
    """
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        Media.__init__(self, title, poster_image_url, trailer_youtube_url)
