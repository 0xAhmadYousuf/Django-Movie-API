import json
from flask import Flask
from flask import request
from flask import jsonify
from functools import wraps
from UMODULES.hash2603 import Hash2603
from UMODULES.mailuserverify import checkusermailconditions

app = Flask(__name__)


def error_handler(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            error_message = str(e)
            # Log the error message for debugging purposes
            print(f"Error: {error_message}")
            return jsonify({'error': 'An unexpected error occurred.'}), 500
    return decorated_function

users = []
movies = []
ratings = []

@error_handler
def load_DB():
    global users, movies, ratings
    try:
        with open('DB/users.json', 'r') as users_file:
            users = json.load(users_file)
        with open('DB/movies.json', 'r') as movies_file:
            movies = json.load(movies_file)
        with open('DB/ratings.json', 'r') as ratings_file:
            ratings = json.load(ratings_file)
    except Exception as e:
        # Log the error message for debugging purposes
        print(f"Error loading data from JSON files: {str(e)}")
        # Handle the error gracefully, optionally initialize with empty lists
        users = []
        movies = []
        ratings = []

load_DB()

@error_handler
def write_DB(UMR="U", data=None):
    global users, movies, ratings
    if UMR == "U" or UMR == "u":
        with open('DB/users.json', 'r') as users_file:
            xusers = json.load(users_file)
        ulen = len(xusers) + 1 # BCZ you'r id sys started from 1 in place of 0
        xdata = {
            # "id":data["id"],
            "id":ulen,
            "name":data["name"],
            "phone":data["phone"],
            "password":data["password"],
            "email":data["email"]
        }
        
        # # Check if email exists or not
        # if not checkusermailconditions(data["email"]):
        #     return jsonify({'message': 'Your email is not valid. Please provide a valid email address.'}), 400
        # # Check if data already exists
        # for user in xusers:
        #     if user["email"] == xdata["email"]:
        #         return jsonify({'message': 'A user with this email already exists.'}), 400
        # # Check for blank fields
        # blank_fields = [key for key, value in xdata.items() if not value]
        # if blank_fields:
        #     return jsonify({'message': f'Incomplete data found. Blank fields: {", ".join(blank_fields)}'}), 400

        xusers.append(xdata)
        users = xusers
        print(xusers)
        with open('DB/users.json', 'w') as users_file:
            json.dump(users, users_file, indent=4)
        
    if UMR == "M" or UMR == "m":
        with open('DB/movies.json', 'r') as movies_file:
            xmovies = json.load(movies_file)
        mlen = len(xmovies) + 1 # BCZ you'r id sys started from 1 in place of 0
        xdata = {
            # "id":data["id"],
            "id":mlen,
            "name":data["name"],
            "genre":data["genre"],
            "rating":data["rating"],
            "release_date":data["release_date"],
        }
        xmovies.append(xdata)
        movies=xmovies
        with open('DB/movies.json', 'w') as movies_file:
            json.dump(movies, movies_file, indent=4)
        
    if UMR == "R" or UMR == "r":
        with open('DB/ratings.json', 'r') as ratings_file:
            xratings = json.load(ratings_file)
        rlen = len(xratings) + 1 # BCZ you'r id sys started from 1 in place of 0
        xdata = {
            # "id":data["id"],
            "id":rlen,
            "user_id":data["user_id"],
            "movie_id":data["movie_id"],
            "rating":data["rating"]
        }
        xratings.append(xdata)
        ratings=xratings
        with open('DB/ratings.json', 'w') as ratings_file:
            json.dump(ratings, ratings_file, indent=4)

@error_handler
def key_maker(email, password, uid=None):
    # Combine username and password to generate a key
    string = f"{email}{password}"
    TMH = Hash2603(string)
    # key = TMH.UR1hash128() # it seams too much big
    key = TMH.UR1hash32()
    str_key = str(uid).zfill(4)
    return f"{key}XPZT{str_key}"
    
@error_handler
def key_check(key):
    # Load user data from JSON file
    with open('DB/users.json', 'r') as users_file:
        users_data = json.load(users_file)
    # Check if the key exists in the list of keys
    for user in users_data:
        uid = user['id']
        email = user['email']
        password = user['password']
        # Generate key
        found_key = key_maker(email, password, uid)
        if key == found_key:
            return True, found_key, user
    return False, None, {}

@error_handler
def authenticate(email, password):
    # Load user data from JSON file
    with open('DB/users.json', 'r') as users_file:
        users_data = json.load(users_file)
    # Check if the User:pass exists in the list of keys
    for user in users_data:
        if user['email'] == email and user['password'] == password:
            uid = user['id']
            email = user['email']
            password = user['password']
            found_key = key_maker(email, password, uid)
            return True, found_key, user
    return  False, None, {}

@error_handler
def okornot(data):
    tf, key, datas = False, None, {}
    try:
        email,password = data['email'], data['password']
        tf, key, datas = authenticate(email=email, password=password)
        return tf, key, datas, 
    except:
        try:
            key = data['key']
            tf, key, datas = key_check(key=key)
            return tf, key, datas
        except:
            return tf, key, datas




##################################################################################
##################################################################################
##################################### Routes #####################################
##################################################################################
##################################################################################
##################################################################################





@app.route('/signup', methods=['POST'])
@error_handler
def signup():
    data = request.json
    # Check if email and password are provided
    if 'email' not in data or 'password' not in data:
        return jsonify({'message': 'Email and password are required fields.'}), 400
    # Check if the email is valid
    if not checkusermailconditions(data["email"]):
        return jsonify({'message': 'Your email is not valid. Please provide a valid email address.'}), 400
    # Check if the email already exists
    for user in users:
        if user["email"] == data["email"]:
            return jsonify({'message': 'A user with this email already exists.'}), 400
    # Check for blank fields
    blank_fields = [key for key, value in data.items() if not value]
    if blank_fields:
        return jsonify({'message': f'Incomplete data found. Blank fields: {", ".join(blank_fields)}'}), 400
    # Generate a unique key for the user
    user_id = len(users) + 1  # Assuming user IDs start from 1
    key = key_maker(data['email'], data['password'], user_id)
    # Add user data to the database
    user_data = {
        "id": user_id,
        "name": data["name"],
        "phone": data["phone"],
        "password": data["password"],
        "email": data["email"]
    }
    users.append(user_data)
    with open('DB/users.json', 'w') as users_file:
        json.dump(users, users_file, indent=4)
    return jsonify({'message': 'User registered successfully.', 'key': key}), 201




# @app.route('/login', methods=['POST'])
# @error_handler
# def login():
#     data = request.json
#     # Check credentials
#     # Assuming simple authentication for demo
#     # If authentication succeeds, return success message
#     tf, key, data = okornot(data=data)
#     if tf:
#         if key_check(key=key):
#             return jsonify({'message': 'Login successful','key':key}), 200
#     else:
#         return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/login', methods=['POST'])
@error_handler
def login():
    data = request.json
    # Check credentials
    # Assuming simple authentication for demo
    # If authentication succeeds, return success message
    tf, key, user_data = okornot(data=data)
    if tf:
        return jsonify({'message': 'Login successful', 'key': key, 'user_data': user_data}), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401


# @app.route('/add_movie', methods=['POST'])
# @error_handler
# def add_movie():
#     data = request.json
#     tf, key, datas = okornot(data=data)
#     if tf:
#         try:
#             write_DB("M", data)
#             return jsonify({'message': 'Wah, movie added in the DB'}), 201
#         except Exception as e:
#             error = str(e)
#             return jsonify({'message': f'key was ok but DB got this error {error}'}), 400
#     else:
#         print(tf, key, datas)
#         return jsonify({'message': 'key was not ok, Unauthorized'}), 401



@app.route('/add_movie', methods=['POST'])
@error_handler
def add_movie():
    data = request.json
    tf, key, user_data = okornot(data=data)
    if tf:
        try:
            write_DB("M", data)
            return jsonify({'message': 'Movie added successfully'}), 201
        except Exception as e:
            error = str(e)
            return jsonify({'message': f'An error occurred: {error}'}), 400
    else:
        print(tf, key, user_data)
        return jsonify({'message': 'Unauthorized access'}), 401









@app.route('/movies', methods=['GET'])
@error_handler
def get_movies():
    return jsonify(movies)

@app.route('/rate_movie', methods=['POST'])
@error_handler
def rate_movie():
    data = request.json
    tf, key, datas = okornot(data=data)
    if tf:
        try:
            ouid = datas['id']
            nuid = data['user_id']
            if data['user_id'] == datas['id']:
                write_DB("R", data)
                return jsonify({'message': 'Wah, movie rating added in the DB'}), 201
            else:
                return jsonify({'message': f'key was on {nuid} ok, Unauthobut used on {ouid}'}), 401
        except Exception as e:
            error = str(e)
            return jsonify({'message': f'key was ok but DB got this error {error}'}), 400
    else:
        print(tf, key, datas)
        return jsonify({'message': f'key was not ok, Unauthorized, {tf} {key}  {datas}'}), 401



@app.route('/search_movie', methods=['GET'])
@error_handler
def search_movie():
    movie_name = request.args.get('name')
    matched_movies = []
    
    # Search for movies with names containing the provided movie_name
    for movie in movies:
        if movie_name.lower() in movie['name'].lower():
            matched_movies.append(movie)

    if matched_movies:
        # Calculate average rating for each matched movie (if ratings are available)
        for movie in matched_movies:
            ratings_sum = 0
            ratings_count = 0
            for rating in ratings:
                if rating['movie_id'] == movie['id']:
                    ratings_sum += rating['rating']
                    ratings_count += 1
            if ratings_count > 0:
                movie['average_rating'] = ratings_sum / ratings_count
            else:
                movie['average_rating'] = None
        
        return jsonify({'matched_movies': matched_movies}), 200
    else:
        return jsonify({'message': 'No movies found matching the provided name.'}), 404


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
@error_handler
def catch_all(path):
    help_json = {
        "message": "Welcome to the Movie Rating System API!",
        "endpoints": {
            "/login": "POST - User login",
            "/add_movie": "POST - Add a movie",
            "/movies": "GET - Get a list of all movies",
            "/rate_movie": "POST - Rate a movie",
            "/search_movie?name={movie_name}": "GET - Search for a movie by name",
            "/help": "GET - View this help message"
        }
    }
    return jsonify(help_json), 404


if __name__ == '__main__':
    app.run(debug=True)