from istorage import IStorage
import json
import os
import requests


class StorageJson(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as movie_data:
                movies = json.loads(movie_data.read())
            json_movies = json.dumps(movies, indent=4)
            with open(self.file_path, "w") as movie_data:
                movie_data.write(json_movies)
        else:
            movies = {}
            titles = ["The Shawshank Redemption",
                      "Pulp Fiction", "The Room",
                      "The Godfather",
                      "The Godfather Part II",
                      "The Dark Knight",
                      "12 Angry Men",
                      "Everything Everywhere All At Once",
                      "Forrest Gump",
                      "Star Wars Episode V"]
            api_key = "93630ab7"
            for title in titles:
                url = f"http://www.omdbapi.com/?apikey={api_key}&t={title}"
                request_movie = requests.get(url)
                movie = request_movie.json()
                movies[movie["Title"]] = {"year": movie["Year"], "rating": movie["imdbRating"], "poster": movie["Poster"]}
            json_movies = json.dumps(movies, indent=4)
            with open(self.file_path, "w") as movie_data:
                movie_data.write(json_movies)


    def list_movies(self):
        """
        Returns a dictionary of dictionaries that
        contains the movies information in the database.
        """
        with open(self.file_path, "r") as movie_data:
            movies = json.loads(movie_data.read())
        return movies


    def add_movie(self, title, year, rating, poster):
        """
        Adds a movie to the movies database.
        Loads the information from the JSON file, add the movie,
        and saves it.
        """
        movies = self.list_movies()
        movies[title] = {"year": year, "rating": rating, "poster" : poster}
        json_movies = json.dumps(movies, indent=4)
        with open(self.file_path, "w") as movie_data:
            movie_data.write(json_movies)


    def delete_movie(self, title):
        """
        Deletes a movie from the movies database.
        Loads the information from the JSON file, deletes the movie,
        and saves it.
        """
        movies = self.list_movies()
        del movies[title]
        json_movies = json.dumps(movies, indent=4)
        with open(self.file_path, "w") as movie_data:
            movie_data.write(json_movies)


    def update_movie(self, title, rating):
        """
        Updates a movie from the movies database.
        Loads the information from the JSON file, updates the movie,
        and saves it.
        """
        movies = self.list_movies()
        movies[title]["rating"] = rating
        json_movies = json.dumps(movies, indent=4)
        with open(self.file_path, "w") as movie_data:
            movie_data.write(json_movies)