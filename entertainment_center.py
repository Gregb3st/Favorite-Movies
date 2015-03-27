import movie
import fresh_tomatoes
import os

#this is the main entry point
#it gets movie from 'Favourite_movies.txt' file which should be located in the same folder
#and gets all necessary details for each movie
#then it represents it on a web page

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
    p = p.rstrip('\n').encode("ascii", "ignore") #preparing line read from the file
    print 'Processing "' + p + '"' #logging the movie processed
    movies.append(movie.Movie(p))
print "Finished Obtaining Favourite Movie Details"

#creating web page with the movies from the list
print "Creating webpage" #logging
fresh_tomatoes.open_movies_page(movies)
print "Finished! :)"

