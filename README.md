# Django URL Shortener

A simple and efficient URL Shortener web application built with Python and Django.

## Overview

This application takes long URLs and generates short, unique links. It stores the mapping in a database and correctly redirects users when they access the shortened URL. 

## Features

- **Long to Short URL Conversion**: Easily convert any valid URL into a compact, easily shareable short link.
- **Unique Link Generation**: Automatically ensures that all generated short codes are unique.
- **Instant Redirection**: Transparently redirects users from a short link to the original target destination.
- **Minimalistic UI**: Clean and straightforward home page interface for creating short links.

## Project Structure

- `core/`: Main Django project configuration settings and root routing.
- `shortener/`: The core app handling the models, views, and routing for URLs.
- `templates/`: HTML templates for the user interface.

## Prerequisites

- [Python](https://www.python.org/downloads/) 3.x
- [Django](https://www.djangoproject.com/) 3.x or higher

## Local Setup & Installation

1. **Clone the repository** (if you haven't already):
   ```bash
   git clone <your-github-repo-url>
   cd "Django Project/url_shortener"
   ```

2. **Set up a Virtual Environment (Optional but Recommended)**:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Dependencies**:
   If there is a `requirements.txt` file (you can generate one with `pip freeze > requirements.txt`), run:
   ```bash
   pip install -r requirements.txt
   ```
   *Otherwise, simply install Django:*
   ```bash
   pip install django
   ```

4. **Apply Database Migrations**:
   Run the following command to set up the SQLite database (the default in Django):
   ```bash
   python manage.py migrate
   ```

5. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the Application**:
   Open your browser and navigate to `http://127.0.0.1:8000/`.

## Usage

1. Open the homepage in your browser.
2. Enter the long URL you want to shorten into the input form.
3. Submit the form to generate your short URL (e.g., `http://127.0.0.1:8000/xYz123`).
4. Share the shortened link. When anyone clicks it, they will be seamlessly redirected to the original long URL!

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## License

This project is open-source and available under the [MIT License](LICENSE).
