# MY CINEMA
This program interacts with the open movie database from OMDb API.
When you start the program, you can choose between the following commands:

### List movies
Prints all the movies, along with their rating.
In addition, the command prints how many movies there are in total in the database.

### Add movie
Asks the user to enter a movie name and a rating and adds it to the database.

### Delete movie
Asks the user to enter a movie name, and deletes it.

### Update movie
Asks the user to enter a movie name, and then checks if it exists.
If it exists, asks the user to enter a new rating, and updates the movie’s rating in the database.

### Stats
Prints statistics like average rating, median rating, best and worst movie in the database.

### Random movie
Prints a random movie and it’s rating.

### Search movie
Asks the user to enter a part of a movie name, and then searches all the movies in the database
and prints all the movies that matched the user’s query, along with the rating.

### Movies sorted by rating
Prints all the movies and their ratings, in descending order by the rating.

### Generate website
Writes the movie data in an html file and generates a website.
You can see the new generated index.html in the website directory and open it.

### Quit the program
Quits the program.

## Installation
To install this project, simply clone the repository and install the dependencies in requirements.txt using `pip`.

## Usage
To create your own Cinema, run the following command - `python main.py`.
To see the new generated files, you may have to run the program twice.