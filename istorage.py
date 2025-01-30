from abc import ABC, abstractmethod


class IStorage(ABC):
    @abstractmethod
    def list_movies(self):
        """
        Prints all the movies, along with their rating.
        In addition, the command prints how many movies there are in total in the database.
        """
        pass


    @abstractmethod
    def add_movie(self, title, year, rating, poster):
        """
        Asks the user to enter a movie name and a rating and adds it to the database.
        """
        pass


    @abstractmethod
    def delete_movie(self, title):
        """
        Asks the user to enter a movie name, and deletes it.
        """
        pass


    @abstractmethod
    def update_movie(self, title, rating):
        """
        Asks the user to enter a movie name, and then checks if it exists.
        If it exists, asks the user to enter a new rating,
        and updates the movie’s rating in the database.
        """
        pass