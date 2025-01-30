from movie_app import MovieApp
from storage_json import StorageJson
from storage_csv import StorageCsv
import requests


def main():
    try:
        storage = StorageJson('movies.json')
        movie_app = MovieApp(storage)
        movie_app.run()
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()