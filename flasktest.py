import requests
import json

BASE_URL = 'http://127.0.0.1:5000'  # Assuming Flask app is running locally on port 5000

# Function to pretty print JSON response
def print_json(response):
    try:
        print(json.dumps(response.json(), indent=4))
    except ValueError:
        print("Response is not in JSON format.")
        print(response.text)

# Function to handle HTTP errors
def handle_http_error(response):
    if response.status_code >= 400:
        print(f"HTTP Error: {response.status_code}")
        print_json(response)
        return True
    return False

# Test signup endpoint
def test_signup():
    try:
        url = f"{BASE_URL}/signup"
        data = {
            "name": "John Doe",
            "phone": "1234567890",
            "email": "john000@example.com",
            "password": "password123"
        }
        response = requests.post(url, json=data)
        if not handle_http_error(response):
            print_json(response)
    except requests.RequestException as e:
        print(f"Request Exception: {e}")

# Test login endpoint
def test_login():
    try:
        url = f"{BASE_URL}/login"
        data = {
            "email": "john000@example.com",
            "password": "password123"
        }
        response = requests.post(url, json=data)
        if not handle_http_error(response):
            print_json(response)
    except requests.RequestException as e:
        print(f"Request Exception: {e}")

# Test add_movie endpoint
def test_add_movie():
    try:
        url = f"{BASE_URL}/add_movie"
        data = {
            "name": "The Matrix",
            "genre": "Science Fiction",
            "rating": 9.0,
            "release_date": "1999-03-31",
            'key': '14587334ae0ff1fd9bd04a5a85110c2fXPZT0001'
        }
        response = requests.post(url, json=data)
        if not handle_http_error(response):
            print_json(response)
    except requests.RequestException as e:
        print(f"Request Exception: {e}")

# Test movies endpoint
def test_get_movies():
    try:
        url = f"{BASE_URL}/movies"
        response = requests.get(url)
        if not handle_http_error(response):
            print_json(response)
    except requests.RequestException as e:
        print(f"Request Exception: {e}")

# Test rate_movie endpoint
def test_rate_movie():
    try:
        url = f"{BASE_URL}/rate_movie"
        data = {
            "user_id": 1,
            "movie_id": 1,
            "rating": 8.,
            'key': '14587334ae0ff1fd9bd04a5a85110c2fXPZT0001'
        }
        response = requests.post(url, json=data)
        if not handle_http_error(response):
            print_json(response)
    except requests.RequestException as e:
        print(f"Request Exception: {e}")

# Test search_movie endpoint
def test_search_movie():
    try:
        url = f"{BASE_URL}/search_movie?name=Endgame"
        response = requests.get(url)
        if not handle_http_error(response):
            print_json(response)
    except requests.RequestException as e:
        print(f"Request Exception: {e}")

# Test catch_all endpoint
def test_catch_all():
    try:
        url = f"{BASE_URL}/nonexistent_endpoint"
        response = requests.get(url)
        if not handle_http_error(response):
            print_json(response)
    except requests.RequestException as e:
        print(f"Request Exception: {e}")

# Run tests
if __name__ == '__main__':
    print("running code for ------------------------------------------    test_signup    -------------------------------------------------------")
    test_signup()
    print("running code for ------------------------------------------    test_login    -------------------------------------------------------")
    test_login()
    print("running code for ------------------------------------------    test_add_movie    -------------------------------------------------------")
    test_add_movie()
    print("running code for ------------------------------------------    test_get_movies    -------------------------------------------------------")
    test_get_movies()
    print("running code for ------------------------------------------    test_rate_movie    -------------------------------------------------------")
    test_rate_movie()
    print("running code for ------------------------------------------    test_search_movie    -------------------------------------------------------")
    test_search_movie()
    print("running code for ------------------------------------------    test_catch_all    -------------------------------------------------------")
    test_catch_all()












# for you this is result which you will get after running the code on flaskapp.py and then this one (1st time)
"""
running code for ------------------------------------------    test_signup    -------------------------------------------------------
{
    "key": "9ed3d4c60951fc9d37c3a3096db4791fXPZT0005",
    "message": "User registered successfully."
}
running code for ------------------------------------------    test_login    -------------------------------------------------------
{
    "key": "9ed3d4c60951fc9d37c3a3096db4791fXPZT0005",
    "message": "Login successful",
    "user_data": {
        "email": "john000@example.com",
        "id": 5,
        "name": "John Doe",
        "password": "password123",
        "phone": "1234567890"
    }
}
running code for ------------------------------------------    test_add_movie    -------------------------------------------------------
HTTP Error: 401
{
    "message": "Unauthorized access"
}
running code for ------------------------------------------    test_get_movies    -------------------------------------------------------
[
    {
        "genre": "Comedy",
        "id": 1,
        "name": "Home Alone",
        "rating": "PG",
        "release_date": "01-04-1996"
    },
    {
        "genre": "Crime",
        "id": 2,
        "name": "The Godfather",
        "rating": "R",
        "release_date": "01-04-1972"
    },
    {
        "genre": "Action",
        "id": 3,
        "name": "Avengers: Endgame",
        "rating": "PG",
        "release_date": "01-04-2019"
    },
    {
        "genre": "Science Fiction",
        "id": 4,
        "name": "The Matrix",
        "rating": 9.0,
        "release_date": "1999-03-31"
    }
]
running code for ------------------------------------------    test_rate_movie    -------------------------------------------------------
HTTP Error: 401
{
    "message": "key was not ok, Unauthorized, False None  {}"
}
running code for ------------------------------------------    test_search_movie    -------------------------------------------------------
{
    "matched_movies": [
        {
            "average_rating": 3.733333333333333,
            "genre": "Action",
            "id": 3,
            "name": "Avengers: Endgame",
            "rating": "PG",
            "release_date": "01-04-2019"
        }
    ]
}
running code for ------------------------------------------    test_catch_all    -------------------------------------------------------
HTTP Error: 404
{
    "endpoints": {
        "/add_movie": "POST - Add a movie",
        "/help": "GET - View this help message",
        "/login": "POST - User login",
        "/movies": "GET - Get a list of all movies",
        "/rate_movie": "POST - Rate a movie",
        "/search_movie?name={movie_name}": "GET - Search for a movie by name"
    },
    "message": "Welcome to the Movie Rating System API!"
}
"""















# for you this is result which you will get after running the code on flaskapp.py and then this one (2nd time)
"""
running code for ------------------------------------------    test_signup    -------------------------------------------------------
HTTP Error: 400
{
    "message": "A user with this email already exists."
}
running code for ------------------------------------------    test_login    -------------------------------------------------------
{
    "key": "14587334ae0ff1fd9bd04a5a85110c2fXPZT0001",
    "message": "Login successful",
    "user_data": {
        "email": "john@example.com",
        "id": 1,
        "name": "John Doe",
        "password": "password123",
        "phone": "1234567890"
    }
}
running code for ------------------------------------------    test_add_movie    -------------------------------------------------------
{
    "message": "Movie added successfully"
}
running code for ------------------------------------------    test_get_movies    -------------------------------------------------------
[
    {
        "genre": "Comedy",
        "id": 1,
        "name": "Home Alone",
        "rating": "PG",
        "release_date": "01-04-1996"
    },
    {
        "genre": "Crime",
        "id": 2,
        "name": "The Godfather",
        "rating": "R",
        "release_date": "01-04-1972"
    },
    {
        "genre": "Action",
        "id": 3,
        "name": "Avengers: Endgame",
        "rating": "PG",
        "release_date": "01-04-2019"
    },
    {
        "genre": "Science Fiction",
        "id": 4,
        "name": "The Matrix",
        "rating": 9.0,
        "release_date": "1999-03-31"
    }
]
running code for ------------------------------------------    test_rate_movie    -------------------------------------------------------
{
    "message": "Wah, movie rating added in the DB"
}
running code for ------------------------------------------    test_search_movie    -------------------------------------------------------
{
    "matched_movies": [
        {
            "average_rating": 3.733333333333333,
            "genre": "Action",
            "id": 3,
            "name": "Avengers: Endgame",
            "rating": "PG",
            "release_date": "01-04-2019"
        }
    ]
}
running code for ------------------------------------------    test_catch_all    -------------------------------------------------------
HTTP Error: 404
{
    "endpoints": {
        "/add_movie": "POST - Add a movie",
        "/help": "GET - View this help message",
        "/login": "POST - User login",
        "/movies": "GET - Get a list of all movies",
        "/rate_movie": "POST - Rate a movie",
        "/search_movie?name={movie_name}": "GET - Search for a movie by name"
    },
    "message": "Welcome to the Movie Rating System API!"
}
"""