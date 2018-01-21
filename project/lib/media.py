import webbrowser

class Movie():
    """This class provides a way to store movie related information"""

    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']

    def __init__(self, movie_title):
        self.movie_title = movie_title

    def show_info(self):
        print(self.movie_title)
