import urllib2
import json

"""This class is used for searching movie details and trailer
it provides getters for the required movie details / trailer id
gets details at http://www.omdbapi.com/
gets trailer id at https://www.youtube.com/yt/dev/en/api-resources.html

Args:
    title (string): the movie title to search details for
"""

class SearchMovieDetails:

    def __init__(self, title):
        #used for get_title error message if no search results found
        self.entered_title = title
        #prepare chosen title for http requests
        self.search_title = title.strip().replace(" ", "+")
        #get all movie details in a json (except trailer id)
        self.movie_details_json = self.get_movie_details_json(
                                                        self.search_title)
        #get json with trailer id
        self.movie_trailer_json = self.get_trailer_json(self.search_title)


    """Methods that request web apis for movie details and trailer"""
    def get_movie_details_json(self, movie_title):
        """Requests omdb api for movie details

        Args:
            movie_title(string): the title of the movie to search details for
                should be proper formatted (trimmed / no spaces inside)

        Returns:
            JSON containing the movie detais

        Raises:
            IOError if http response has invalid status code / timeout
        """
        url = "http://www.omdbapi.com/?t=" + movie_title \
                                            + "&y=&plot=short&r=json"

        try:
            r = json.load(urllib2.urlopen(url))
            #print 'Movie details found for "' + self.entered_title + '"!'
        except IOError:
            r = "No results found"
            print 'Failed accessing omdb api for "' + self.entered_title + '"!'
            print "url = " + url
            print "Try checking internet connection"

        return r

    def get_trailer_json(self, movie_title):
        """Requests youtube for official movie trailer

        Args:
            movie_title(string): the title of the movie to search details for
                should be proper formatted (trimmed / no spaces inside)

        Returns:
            JSON containing the trailer detais

        Raises:
            IOError if http response has invalid status code / timeout
        """
        search_string = movie_title + "+official+trailer"
        api_key = "AIzaSyD0Ed38kbKXxTX2VH2wlzxpb516n4U2LRw"
        url = "https://www.googleapis.com/youtube/v3/search?" \
                        + "part=id&maxResults=1&q=" + search_string \
                        + "&key=" + api_key

        try:
            r = json.load(urllib2.urlopen(url))
            #print "Movie Trailer ID found for " + self.entered_title + "!"
        except IOError:
            r = "No results found!"
            print 'Failed accessing youtube api for "' \
                                                + self.entered_title + '"!'
            print "url = " + url
            print "Please check internet connection / youtube api key"

        return r


    """Getters for various details from the 2 jsons got from web"""
    def get_youtube_id(self):
        """Gets youtube trailer id from movie_trailer_json

        Returns:
            youtube trailer id(string)

        Raises:
            If unsuccessful returns "not found" message as well as
            youtube id of "not found" trailer
        """
        try:
            r = self.movie_trailer_json['items'][0]['id']['videoId']
            #deprecated: fresh_tomatoes.py id handling was updated
            #r = "https://www.youtube.com/watch?v=" + r
            #print 'Successfully got Trailer ID for "' \
                                            #+ self.entered_title + '"!'
        except:
            # r = "No results found"
            r = "PMKE-Tm0Bes" #No results found trailer id
            print 'Trailer ID not found for "' + self.entered_title + '"!'

        return r


    def get_year (self):
        """Gets movie year from movie_details_json

        Returns:
            Year(string)

        Raises:
            If unsuccessful returns "not found" message
        """
        try:
            r = self.movie_details_json['Year']
            #print 'Successfully got Year for "' + self.entered_title + '"!'
        except:
            r = "No results found"
            print 'Year not found for "' + self.entered_title + '"!'

        return r

    def get_genre (self):
        """Gets movie genre from movie_details_json

        Returns:
            Genre(string)

        Raises:
            If unsuccessful returns "not found" message
        """
        try:
            r = self.movie_details_json['Genre'].encode("ascii", "ignore")
            #print 'Successfully got Genre info for "' \
                                            #+ self.entered_title + '"!'
        except:
            r = "No results found"
            print 'Genre info not found for "' + self.entered_title + '"!'

        return r

    def get_plot (self):
        """Gets movie plot from movie_details_json

        Returns:
            Plot(string)

        Raises:
            If unsuccessful returns "not found" message
        """
        try:
            r = self.movie_details_json['Plot'].encode("ascii", "ignore")
            #print 'Successfully got Plot for "' + self.entered_title + '"!'
        except:
            r = "No results found"
            print 'Plot not found for "' + self.entered_title + '"!'

        return r

    def get_actors (self):
        """Gets movie actors from movie_details_json

        Returns:
            Actors(string)

        Raises:
            If unsuccessful returns "not found" message
        """
        try:
            r = self.movie_details_json['Actors'].encode("ascii", "ignore")
            #print 'Successfully got Actors for "' + self.entered_title + '"!'
        except:
            r = "No results found"
            print 'Actors not found for "' + self.entered_title + '"!'

        return r

    def get_awards (self):
        """Gets movie awards from movie_details_json

        Returns:
            Awards(string)

        Raises:
            If unsuccessful returns "not found" message
        """
        try:
            r = self.movie_details_json['Awards'].encode("ascii", "ignore")
            #print 'Successfully got Awards for "' + self.entered_title + '"!'
        except:
            r = "No results found"
            print 'Awards not found for "' + self.entered_title + '"!'

        return r

    def get_rating (self):
        """Gets movie rating from movie_details_json

        Returns:
            Rating

        Raises:
            If unsuccessful returns "not found" message
        """
        try:
            r = self.movie_details_json['imdbRating']
            #print 'Successfully got imdbRating for "' \
                                                #+ self.entered_title + '"!'
        except:
            r = "No results found"
            print 'imdbRating not found for "' + self.entered_title + '"!'

        return r

    def get_votes (self):
        """Gets movie votes from movie_details_json

        Returns:
            Votes

        Raises:
            If unsuccessful returns "not found" message
        """
        try:
            r = self.movie_details_json['imdbVotes'].replace(","," ")
            #print 'Successfully got imdbVotes for "' \
                                                #+ self.entered_title + '"!'
        except:
            r = "No results found"
            print 'imdbVotes not found for "' + self.entered_title + '"!'

        return r

    def get_title (self):
        """Gets movie proper title from movie_details_json
        Also returns a message if no movie with such title found, advising to
        check it.

        Returns:
            Movie Title(string)

        Raises:
            If unsuccessful returns "not found" message
        """
        try:
            r = self.movie_details_json['Title'].encode("ascii", "ignore")
            #print 'Successfully got Movie Title for "' \
                                                #+ self.entered_title + '"!'
        except:
            r = 'No results found for: "' + self.entered_title \
                        + '". Check the title entered in Favourite_movies.txt'
            print '!!! No Movie With Such Title Found "' \
                                                + self.entered_title + '" !!!'
            print "Please, check Movie Title entered in" \
                                        + "Favourite_Movies.txt file"

        return r

    def get_poster (self):
        """Gets movie poster from movie_details_json

        Returns:
            Link to poster image of the movie(string)

        Raises:
            If unsuccessful returns "not found" message
        """
        try:
            r = self.movie_details_json['Poster']
            #print 'Successfully got Poster for "' \
                                                #+ self.entered_title + '"!'
        except:
            #No image found url
            r = 'Poster not found for "' + self.entered_title + '"'
            print 'Poster not found for "' + self.entered_title + '"!'

        return r
