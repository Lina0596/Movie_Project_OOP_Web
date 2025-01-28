from istorage import IStorage
import json


class StorageJson(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path
        self.movies = {}
        json_movies = json.dumps(self.movies, indent=4)
        with open (self.file_path, "w") as movie_data:
            movie_data.write(json_movies)

    def list_movies(self):
        """
        Returns a dictionary of dictionaries that
        contains the movies information in the database.
        """

        with open(self.file_path, "r") as movie_data:
            movies = json.loads(movie_data.read())
        return movies

    def add_movie(self, title, year, rating):
        """
        Adds a movie to the movies database.
        Loads the information from the JSON file, add the movie,
        and saves it.
        """
        movies = self.list_movies()
        movies[title] = {"year": year, "rating": rating}
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


def main():
    pass


if __name__ == "__main__":
    main()