import search_movie_details

"""This class makes all details of a single movie to be available to use
It uses movie title provided to search for movie details in web using
search_movie_details.py

Args:
    title(string): title of a movie
"""

class Movie():

    def __init__ (self, title):
        print 'Searching for movie details in web for "' + title + '"...'
        details = search_movie_details.SearchMovieDetails(title)
        print 'Getting the results for "' + title + '"...'
        print 'Getting Movie Title for "' + title + '"...'
        self.title = details.get_title()
        print 'Getting Storyline (Plot) for "' + title + '"...'
        self.storyline = details.get_plot()
        print 'Getting Poster Image for "' + title + '"...'
        self.poster_image_url = details.get_poster()
        print 'Getting Youtube ID for "' + title + '"...'
        self.trailer_youtube_id = details.get_youtube_id()
        print 'Getting Year for "' + title + '"...'
        self.year = details.get_year()
        print 'Getting Genre for "' + title + '"...'
        self.genre = details.get_genre()
        print 'Getting Actors for "' + title + '"...'
        self.actors = details.get_actors()
        print 'Getting Awards for "' + title + '"...'
        self.awards = details.get_awards()
        print 'Getting Rating for "' + title + '"...'
        self.rating = details.get_rating()
        print 'Getting Votes for "' + title + '"...'
        self.votes = details.get_votes()
        print 'Finished searching for "' + title + '" Movie details!'
