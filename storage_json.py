from istorage import IStorage
import json
import os


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
            self.movies = {
                "The Shawshank Redemption": {"year": 1994, "rating": 9.5},
                "Pulp Fiction": {"year": 1994, "rating": 8.8},
                "The Room": {"year": 2003, "rating": 3.6},
                "The Godfather": {"year": 1972, "rating": 9.2},
                "The Godfather Part II": {"year": 1974, "rating": 9.0},
                "The Dark Knight": {"year": 2008, "rating": 9.0},
                "12 Angry Men": {"year": 1957, "rating": 8.9},
                "Everything Everywhere All At Once": {"year": 2022, "rating": 8.9},
                "Forrest Gump": {"year": 1994, "rating": 8.8},
                "Star Wars Episode V": {"year": 1980, "rating": 8.7}
            }
            json_movies = json.dumps(self.movies, indent=4)
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