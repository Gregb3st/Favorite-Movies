import movie
import fresh_tomatoes
import os

"""This is the main entry point
it gets movie from 'Favourite_movies.txt' file which should be located in
the same folder and gets all necessary details for each movie. Then it
represents all the movies and their details on a web page.
Clicking on a movie tile will show the official trailer.
"""

#creating movies list
movies = []

#getting file path (relative) and reading it
fn = os.path.join(os.path.dirname(__file__), 'Movies_list.txt')
print "Trying to read the file located at"
print fn
with open(fn) as f:
    content = f.readlines()

#getting all movies' details and appending to the movies list
print "Obtaining Favorite Movies  details..."
for p in content:
    #reading and preparing the line from the file
    p = p.rstrip('\n').encode("ascii", "ignore")
    print 'Processing "' + p + '"' #logging the movie processed
    movies.append(movie.Movie(p))
print "Finished Obtaining Favourite Movie Details"

#creating web page with the movies from the list
print "Creating webpage" #logging
fresh_tomatoes.open_movies_page(movies)

print "Finished! :)"
