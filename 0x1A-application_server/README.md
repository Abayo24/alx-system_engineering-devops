# AirBnB Clone Project

This is a simplified clone of the AirBnB web application built with Flask, a lightweight Python web framework. The project is designed to provide a basic understanding of web development concepts using Flask, including routing, templates, and API development.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Features

- User authentication and authorization
- CRUD operations for listings
- Search functionality
- Booking system
- Basic user interface with HTML/CSS templates

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/AirBnB_clone_v2.git
    cd AirBnB_clone_v2
    ```

2. **Create a virtual environment:**
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up the environment variables:**
    Create a `.env` file and add the necessary environment variables. For example:
    ```sh
    FLASK_APP=web_flask
    FLASK_ENV=development
    SECRET_KEY=your_secret_key
    ```

5. **Initialize the database:**
    ```sh
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

## Usage

1. **Run the Flask application:**
    ```sh
    flask run
    ```
    By default, the application will run on `http://127.0.0.1:5000/`. If port 5000 is in use, you can specify a different port:
    ```sh
    flask run --port=8000
    ```

2. **Access the application in your web browser:**
    Navigate to `http://127.0.0.1:5000/` (or the specified port).


## API Endpoints

### User Authentication

- `POST /api/v1/auth/register`: Register a new user
- `POST /api/v1/auth/login`: Login a user
- `POST /api/v1/auth/logout`: Logout a user

### Listings

- `GET /api/v1/listings`: Get all listings
- `POST /api/v1/listings`: Create a new listing
- `GET /api/v1/listings/<id>`: Get a specific listing
- `PUT /api/v1/listings/<id>`: Update a listing
- `DELETE /api/v1/listings/<id>`: Delete a listing

### Bookings

- `GET /api/v1/bookings`: Get all bookings
- `POST /api/v1/bookings`: Create a new booking
- `GET /api/v1/bookings/<id>`: Get a specific booking
- `PUT /api/v1/bookings/<id>`: Update a booking
- `DELETE /api/v1/bookings/<id>`: Delete a booking

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes. Make sure to follow the coding style and include tests for any new features or bug fixes.

1. **Fork the repository:**
    Click the "Fork" button at the top right of this page.

2. **Clone your fork:**
    ```sh
    git clone https://github.com/yourusername/AirBnB_clone_v2.git
    cd AirBnB_clone_v2
    ```

3. **Create a branch for your changes:**
    ```sh
    git checkout -b my-feature-branch
    ```

4. **Make your changes and commit them:**
    ```sh
    git add .
    git commit -m "Add my feature"
    ```

5. **Push to your fork and submit a pull request:**
    ```sh
    git push origin my-feature-branch
    ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

