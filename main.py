from Movie_Project_OOP_Web.storage.storage_json import StorageJson
from movie_app import MovieApp
from Movie_Project_OOP_Web.storage.storage_csv import StorageCsv


def main():
    try:
        storage = StorageJson('movies.json')
        movie_app = MovieApp(storage)
        movie_app.run()
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()