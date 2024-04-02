![image](https://github.com/0xAhmadYousuf/Flask-Movie-API/assets/139548576/9d5b8af9-9640-4875-9535-0ae4816f978a)


# Flask-Movie-API
## Movie Rating System API Documentation

### Language and Database
- **Language**: Python
- **Database**: JSON files (`users.json`, `movies.json`, `ratings.json`)
- **Reason**: JSON files are used as a simple and lightweight solution for storing user, movie, and rating data. They provide easy readability and flexibility, making them suitable for this project's requirements.

### Project Repository
- You can find the project repository at [Flask-Movie-API](https://github.com/0xAhmadYousuf/Flask-Movie-API). It's a Flask-based implementation of a Movie API with similar functionalities.

### Setup Instructions
1. Ensure you have Python installed on your system.
2. Clone or download the project repository from [GitHub](https://github.com/0xAhmadYousuf/Flask-Movie-API).
3. Install required dependencies by running `pip install -r requirements.txt`.
4. Run the Flask development server using `python manage.py runserver`.
5. The API will be accessible at `http://localhost:5000`.

### Assumptions
- User IDs start from 1 and increment sequentially.
- User authentication is based on email and password combination.
- Each movie and user rating is associated with a unique identifier, and IDs increment sequentially.
- The system uses a simple hash-based authentication mechanism for generating and verifying keys.

### Problem Solving
- **Implemented Features**:
  - User registration (`/signup` endpoint)
  - User authentication (`/login` endpoint)
  - Adding movies to the database (`/add_movie` endpoint)
  - Retrieving a list of all movies (`/movies` endpoint)
  - Rating movies (`/rate_movie` endpoint)
  - Searching for movies by name (`/search_movie` endpoint)
  - Error handling using decorators (`@error_handler`)
- **Remaining Tasks**:
  - Implementing login functionality.
  - Adding error handling and validation for different endpoints.
  - Enhancing security measures such as password hashing.
  - Improving efficiency and scalability of the database operations.

### Problems Faced and Solutions
- **Problem**: Need to handle errors and exceptions uniformly across different endpoints.
  - **Solution**: Implemented a decorator `@error_handler` to catch and handle exceptions gracefully, providing consistent error responses.

- **Problem**: Ensuring uniqueness of user email addresses and preventing duplicate entries.
  - **Solution**: Added logic to check for existing email addresses during user registration and return appropriate error messages if duplication is detected.

- **Problem**: Generating and validating keys for user authentication.
  - **Solution**: Created functions `key_maker()` and `key_check()` to generate and verify keys based on user email and password combinations. This ensures secure authentication and authorization.

- **Problem**: Handling user input validation and ensuring completeness of required fields.
  - **Solution**: Implemented checks to validate input data for user registration and movie addition endpoints, ensuring that essential fields are provided and not left blank.

### File Structure
```
flaskapp.
project_root/
______________________________________________________________________________________
  ├── UMODULES/
  │   ├── __pycache__/  # Contains bytecode-compiled files generated by Python
  │   │   ├── hash2603.cpython-311.pyc
  │   │   └── mailuserverify.cpython-311.pyc
  │   ├── hash2603.py
  │   └── mailuserverify.py
  ├── DB/
  │  ├── movies.json  # JSON file storing movie data
  │  ├── ratings.json  # JSON file storing movie ratings data
  │  └── users.json  # JSON file storing user data
  │
  ├── README.md  # Optional file containing project documentation
  ├── requirements.txt  # Optional file containing project modules list to install
  ├── flaskapp.py  # Main Flask application file
  └── flasktest.py  # Potentially for unit testing using Flask's built-in testing features


```

### Routes
The following routes are available in the API:

- **POST `/signup`**: Register a new user.
- **POST `/login`**: Authenticate a user.
- **POST `/add_movie`**: Add a new movie to the database.
- **GET `/movies`**: Retrieve a list of all movies.
- **POST `/rate_movie`**: Rate a movie.
- **GET `/search_movie?name={movie_name}`**: Search for movies by name.

For more details on each endpoint and their usage, refer to the help message provided at the root endpoint (`/`).

---

Feel free to explore the [Flask-Movie-API](https://github.com/0xAhmadYousuf/Flask-Movie-API) repository for further insights into a Flask-based implementation of a similar Movie API! If you have any questions or need assistance, don't hesitate to ask.
