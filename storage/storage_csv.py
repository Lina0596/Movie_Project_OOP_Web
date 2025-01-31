from Movie_Project_OOP_Web.storage.istorage import IStorage
import os
import requests


class StorageCsv(IStorage):
    def __init__(self, file_path):
        self.file_path = f"data/{file_path}"
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as movie_data:
                movies = movie_data.read()
            with open (self.file_path, "w") as movie_data:
                movie_data.write(movies)
        else:
            movies = "Title,Year,Rating,Poster\n"
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
                movies += f"{movie["Title"]},{movie["Year"]},{movie["imdbRating"]},{movie["Poster"]}\n"
            with open (self.file_path, "w") as movie_data:
                movie_data.write(movies)

    def __getitem__(self, item):
        return


    def list_movies(self):
        """
        Returns a dictionary of dictionaries that
        contains the movies information in the database.
        """
        with open(self.file_path, "r") as movie_data:
            movies = {}
            lines = movie_data.readlines()
            for movie in lines[1:]:
                split_line = movie.split(",")
                title = split_line[0]
                year = split_line[1]
                rating = split_line[2]
                poster = split_line[3][:-1]
                movies[title] = {"year": year, "rating": rating, "poster": poster}
            return movies


    def add_movie(self, title, year, rating, poster):
        """
        Adds a movie to the movies database.
        Loads the information from the JSON file, add the movie,
        and saves it.
        """
        with open(self.file_path, "r") as movie_data:
            movies = movie_data.read()
        with open(self.file_path, "w") as movie_data:
            movie_data.write(movies)
            movie_data.write(f"{title},{year},{rating},{poster}\n")


    def delete_movie(self, title):
        """
        Deletes a movie from the movies database.
        Loads the information from the JSON file, deletes the movie,
        and saves it.
        """
        movies = self.list_movies()
        del movies[title]
        updated_movies = ""
        for movie, movie_info in movies.items():
            updated_movies += f"{movie},{movie_info["year"]},{movie_info["rating"]}\n"
        with open(self.file_path, "w") as movie_data:
            movie_data.write("Title,Year,Rating\n")
            movie_data.write(updated_movies)


    def update_movie(self, title, rating):
        """
        Updates a movie from the movies database.
        Loads the information from the JSON file, updates the movie,
        and saves it.
        """
        movies = self.list_movies()
        movies[title]["rating"] = rating
        updated_movies = ""
        for movie, movie_info in movies.items():
            updated_movies += f"{movie},{movie_info["year"]},{movie_info["rating"]}\n"
        with open(self.file_path, "w") as movie_data:
            movie_data.write("Title,Year,Rating\n")
            movie_data.write(updated_movies)

