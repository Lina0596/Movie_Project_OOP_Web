import statistics
import random
import requests


class MovieApp:
    def __init__(self, storage):
        self._storage = storage


    def _list_movies(self):
        """
        Prints all the movies, along with their rating.
        In addition, the command prints how many movies there are in total in the database.
        """
        movies = self._storage.list_movies()
        print(f"\n{len(movies)} movies in total")
        for movie, movie_info in movies.items():
            print(f"{movie} ({movie_info["year"]}): {movie_info["rating"]}")


    def _add_movie(self):
        """
        Asks the user to enter a movie name and a rating and adds it to the database.
        """
        try:
            movies = self._storage.list_movies()
            title = input("\nEnter the name of the movie: ")
            if title == "":
                raise ValueError("You entered an empty title")
            elif title in movies:
                print(f"Movie {title} already exists!")
            else:
                api_key = "93630ab7"
                url = f"http://www.omdbapi.com/?apikey={api_key}&t={title}"
                request_movie = requests.get(url)
                movie = request_movie.json()
                if movie["Response"] == "True":
                    title = movie["Title"]
                    year = movie["Year"]
                    rating = movie["imdbRating"]
                    poster = movie["Poster"]
                    self._storage.add_movie(title, year, rating, poster)
                    print(f"\nYou've added the movie '{title}'")
                elif movie["Response"] == "False":
                    print(f"\n{movie["Error"]}")
        except requests.exceptions.ConnectionError:
            print("We can not connect with the API...")


    def _delete_movie(self):
        """
        Asks the user to enter a movie name, and deletes it.
        """
        movies = self._storage.list_movies()
        valid_title = False
        while not valid_title:
            title = input("\nEnter the name of the movie you want to delete: ")
            if title not in movies:
                raise ValueError("Movie is not in dictionary.")
            elif title in movies:
                self._storage.delete_movie(title)
                print(f"\nYou've delete the movie '{title}'.")
                valid_title = True


    def _update_movie(self):
        """
        Asks the user to enter a movie name, and then checks if it exists.
        If it exists, asks the user to enter a new rating,
        and updates the movie’s rating in the database.
        """
        movies = self._storage.list_movies()
        valid_title = False
        while not valid_title:
            try:
                title = input("\nEnter the name of the movie you want to update: ")
                if title not in movies:
                    raise ValueError("Movie is not in dictionary.")
                elif title in movies:
                    valid_title = True
            except ValueError as e:
                print(f"Invalid input: {e}")
        valid_rating = False
        while not valid_rating:
            try:
                rating = float(input("Enter the new rating of the movie (1-10): "))
                if rating < 1 or rating > 10:
                    raise ValueError("Please enter a rating between 1 and 10.")
                valid_rating = True
            except ValueError as e:
                print(f"Invalid input: {e}")
        self._storage.update_movie(title, rating)
        print(f"\nYou've updated the movie '{title}' with a rating of {rating}.")


    def _stats_movies(self):
        """
        Prints statistics about the movies in the database.
        """
        movies = self._storage.list_movies()

        # Calculates the average of the ratings
        sum_val = 0
        for movie, movie_info in movies.items():
            sum_val += float(movie_info["rating"])
        average_rating = sum_val / len(movies)

        # Calculates the median of the ratings
        listed_ratings = []
        for movie, movie_info in movies.items():
            listed_ratings.append(float(movie_info["rating"]))
        median_rating = statistics.median(listed_ratings)

        # Calculates the best rated and the worst rated movies
        max_rating = max(float(details["rating"]) for details in movies.values())
        best_movies = [(title, details["rating"]) for title, details in movies.items() if float(details["rating"]) == max_rating]
        min_rating = min(float(details["rating"]) for details in movies.values())
        worst_movies = [(title, details["rating"]) for title, details in movies.items() if float(details["rating"]) == min_rating]

        # Displays the stats of the movie dictionary
        print(f"\nAverage rating: {average_rating}")
        print(f"Median rating: {median_rating}")
        print(f"Best movies:")
        for movie, rating in best_movies:
            print(f"{movie}, {rating}")
        print(f"Worst movies:")
        for movie, rating in worst_movies:
            print(f"{movie}, {rating}")


    def _random_movie(self):
        """
        Prints a random movie and it’s rating.
        """
        movies = self._storage.list_movies()
        listed_items = list(movies.items())
        random_movie_title, random_movie_infos = random.choice(listed_items)
        print(f"\n{random_movie_title}: {random_movie_infos["rating"]}")


    def _search_movie(self):
        """
        Asks the user to enter a part of a movie name,
        and then searches all the movies in the database
        and prints all the movies that matched the user’s query, along with the rating.
        """
        movies = self._storage.list_movies()
        part_of_name_movie = input("\nEnter a part of the movie name: ")
        for movie, movie_info in movies.items():
            if part_of_name_movie.lower() in movie.lower():
                print(f"{movie}: {movie_info["rating"]}")


    def _sorting_movies(self):
        """
        Prints all the movies and their ratings, in descending order by the rating.
        """
        movies = self._storage.list_movies()
        copy_of_dictionary_of_movies = movies.copy()
        for i in range(len(copy_of_dictionary_of_movies)):
            most_frequent_movie = ""
            most_frequent_rating = 0
            for movie, movie_info in copy_of_dictionary_of_movies.items():
                if float(movie_info["rating"]) >= most_frequent_rating:
                    most_frequent_movie = movie
                    most_frequent_rating = float(movie_info["rating"])
            print(f"{most_frequent_movie}: {most_frequent_rating}")
            del copy_of_dictionary_of_movies[most_frequent_movie]


    def _generate_website(self):
        """
        Writes the movie data in a html file and generates a website.
        """
        movies = self._storage.list_movies()
        content = ''
        for movie, movie_info in movies.items():
            content += '<li>\n'
            content += '  <div class="movie">\n'
            content += '      <img class="movie-poster"\n'
            content += f'          src={movie_info["poster"]}/>\n'
            content += f'      <div class="movie-title">{movie}</div>\n'
            content += f'      <div class="movie-year">{movie_info["year"]}</div>\n'
            content += '  </div>\n'
            content += '</li>\n'
        with open("website/index_template.html", "r") as template_html_data:
            template_html_data = template_html_data.read()
            new_html_data = template_html_data.replace("__TEMPLATE_MOVIE_GRID__", content)
        with open("website/index.html", "w") as html_file:
            html_file.write(new_html_data)
        print("Website was generated successfully.")


    def run(self):
        print("MY MOVIE DATABASE")

        menu = [
            "\nMenu",
            "0. Quit the program",
            "1. List movies",
            "2. Add movie",
            "3. Delete movie",
            "4. Update movie",
            "5. Stats",
            "6. Random movie",
            "7. Search movie",
            "8. Movies sorted by rating",
            "9. Generate website"
        ]

        running_program = True
        while running_program:
            try:
                print("\n".join(menu))
                user_choose_option = int(input("\nChoose an option from the menu (0-9): "))
                if user_choose_option < 0 or user_choose_option > 9:
                    raise ValueError("Please choose an option between 0 and 9.")
                if user_choose_option == 1:
                    self._list_movies()
                    input("\nPress ENTER to continue...")
                elif user_choose_option == 2:
                    self._add_movie()
                    input("\nPress ENTER to continue...")
                elif user_choose_option == 3:
                    self._delete_movie()
                    input("\nPress ENTER to continue...")
                elif user_choose_option == 4:
                    print("Functionality to update a movie is currently not available.")
                    input("\nPress ENTER to continue...")
                elif user_choose_option == 5:
                    self._stats_movies()
                    input("\nPress ENTER to continue...")
                elif user_choose_option == 6:
                    self._random_movie()
                    input("\nPress ENTER to continue...")
                elif user_choose_option == 7:
                    self._search_movie()
                    input("\nPress ENTER to continue...")
                elif user_choose_option == 8:
                    self._sorting_movies()
                    input("\nPress ENTER to continue...")
                elif user_choose_option == 9:
                    self._generate_website()
                    input("\nPress ENTER to continue...")
                elif user_choose_option == 0:
                    print("\nBye!")
                    running_program = False
            except ValueError as e:
                print(f"Invalid input: {e}")
