from istorage import IStorage
import os


class StorageCsv(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as movie_data:
                movies = movie_data.read()
            with open (self.file_path, "w") as movie_data:
                movie_data.write(movies)
        else:
            movies = ("Title,Year,Rating,Poster\n"
                      "The Shawshank Redemption,1994,9.5\n"
                      "Pulp Fiction,1994,8.8\n"
                      "The Room,2003,3.6\n"
                      "The Godfather,1972,9.2\n"
                      "The Godfather Part II,1974,9.0\n"
                      "The Dark Knight,2008,9.0\n"
                      "12 Angry Men,1957,8.9\n"
                      "Everything Everywhere All At Once,2022,8.9\n"
                      "Forrest Gump,1994,8.8\n"
                      "Star Wars Episode V,1980,8.7\n"
                      )
            with open (self.file_path, "w") as movie_data:
                movie_data.write(movies)


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
                rating = split_line[2][:-1]
                movies[title] = {"year": year, "rating": rating}
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

