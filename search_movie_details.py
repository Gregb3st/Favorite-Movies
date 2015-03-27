import urllib2
import json
import re

#This class is used for searching movie details and trailer
#it provides getters for the required movie details / trailer id
#gets details at omdb
#gets trailer id at youtube
#parameter is movie title (string)

class SearchMovieDetails:

    def __init__(self, title):
        self.entered_title = title #used fr get_title if no search results found
        self.search_title = title.strip().replace(" ", "+") #prepare chosen title for http requests
        self.movie_details_json = self.get_movie_details_json(self.search_title) #get all movie details in a json (except trailer id)
        self.movie_trailer_json = self.get_trailer_json(self.search_title) #get trailer id
    
    #get movie details from omgb in JSON format
    def get_movie_details_json(self, movie_title):

        url = "http://www.omdbapi.com/?t=" + movie_title + "&y=&plot=short&r=json"

        try:
            r = json.load(urllib2.urlopen(url))
            print 'Movie details found for "' + self.entered_title + '"!'
        except IOError:
            r = "No results found"
            print 'Failed accessing omdb api for "' + self.entered_title + '"!'
            print "url = " + url
            print "Try checking internet connection"
            
        return r

    #get trailer details from youtube in json format
    def get_trailer_json(self, movie_title):

        search_string = movie_title + "+official+trailer"
        api_key = "AIzaSyD0Ed38kbKXxTX2VH2wlzxpb516n4U2LRw"
        url = "https://www.googleapis.com/youtube/v3/search?part=id&maxResults=1&q=" + search_string + "&key=" + api_key
 
        try:
            r = json.load(urllib2.urlopen(url))
            print "Movie Trailer ID found for " + self.entered_title + "!"
        except IOError:
            r = "No results found!"
            print 'Failed accessing youtube api for "' + self.entered_title + '"!'
            print "url = " + url
            print "Please check internet connection / youtube api key"

        return r

    # Getters for various details from the 2 jsons
    def get_youtube_id(self):
        
        try:
            r = self.movie_trailer_json['items'][0]['id']['videoId']
            #r = "https://www.youtube.com/watch?v=" + r #to do: update youtube id handling in fresh_tomatoes.py
            print 'Successfully got Trailer ID for "' + self.entered_title + '"!'
        except:
            # r = "No results found"
            r = "PMKE-Tm0Bes" #No results found
            print 'Trailer ID not found for "' + self.entered_title + '"!'

        return r


    def get_year (self):
        try:
            r = self.movie_details_json['Year']
            print 'Successfully got Year for "' + self.entered_title + '"!'
        except:
            r = "No results found"
            print 'Year not found for "' + self.entered_title + '"!'

        return r


    def get_genre (self):
        
        try:
            r = self.movie_details_json['Genre'].encode("ascii", "ignore")
            print 'Successfully got Genre info for "' + self.entered_title + '"!'
        except:
            r = "No results found"
            print 'Genre info not found for "' + self.entered_title + '"!'

        return r


    def get_plot (self):
        
        try:
            r = self.movie_details_json['Plot'].encode("ascii", "ignore")
            print 'Successfully got Plot for "' + self.entered_title + '"!'
        except:
            r = "No results found"
            print 'Plot not found for "' + self.entered_title + '"!'

        return r


    def get_actors (self):
        
        try:
            r = self.movie_details_json['Actors'].encode("ascii", "ignore")
            print 'Successfully got Actors for "' + self.entered_title + '"!'
        except:
            r = "No results found"
            print 'Actors not found for "' + self.entered_title + '"!'

        return r


    def get_awards (self):
        
        try:
            r = self.movie_details_json['Awards'].encode("ascii", "ignore")
            print 'Successfully got Awards for "' + self.entered_title + '"!'
        except:
            r = "No results found"
            print 'Awards not found for "' + self.entered_title + '"!'

        return r

    def get_rating (self):
        
        try:
            r = self.movie_details_json['imdbRating']
            print 'Successfully got imdbRating for "' + self.entered_title + '"!'
        except:
            r = "No results found"
            print 'imdbRating not found for "' + self.entered_title + '"!'

        return r

    def get_votes (self):
        
        try:
            r = self.movie_details_json['imdbVotes'].replace(","," ")
            print 'Successfully got imdbVotes for "' + self.entered_title + '"!'
        except:
            r = "No results found"
            print 'imdbVotes not found for "' + self.entered_title + '"!'

        return r

    def get_title (self):
        
        try:
            r = self.movie_details_json['Title'].encode("ascii", "ignore")
            print 'Successfully got Movie Title for "' + self.entered_title + '"!'
        except:
            r = 'No results found for: "' + self.entered_title + '". Check the title entered in Favourite_movies.txt'
            print '!!! No Movie With Such Title Found "' + self.entered_title + '"!!!'
            print "Please, check Movie Title entered in Favourite_Movies.txt file"

        return r

    def get_poster (self):
        
        try:
            r = self.movie_details_json['Poster']
            print 'Successfully got Poster for "' + self.entered_title + '"!'
        except:
            r = "No results found"
            print 'Poster not found for "' + self.entered_title + '"!'

        return r
