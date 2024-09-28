import requests

key = '60f33c28bafb0b9d8e8f36c06fa5c1b4'
website = "https://api.themoviedb.org/3/search/movie"
api_access_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2MGYzM2MyOGJhZmIwYjlkOGU4ZjM2YzA2ZmE1YzFiNCIsIm5iZiI6MTcyNzQwMDMzMi4zMjYyNTcsInN1YiI6IjY2ZjYwOGQwYjlmZDI3NjI3OTUwOTI2NSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.PYYCc_x9arbNfNpt1pkejq4C62OAj3DV0XvApWMlAKA"


movie = input("Please type a movie: ")


def search_movie(movie):
    params = {
        "api_key": key,
        "query": movie,
        "language": "en_US"
    }

    response = requests.get(url=website, params=params)
    if response.status_code == 200:
        data = response.json()
        if data["results"]:
            for result in data["results"]:
                print(f"Title: {result['title']} Year: {result['release_date']}")

        else:
            print("No result found, try again.")
    else:
        print(f"Error: {response.status_code}")


search_movie(movie)
