# 🔗 Django URL Shortener

A clean, simple, and efficient URL Shortener web application built with **Python** and **Django** that converts long URLs into short, shareable links with instant redirection.

<p align="center">
<a href="https://djshort.onrender.com"><img src="https://img.shields.io/badge/🚀%20Live%20Demo-Visit%20Website-2ea44f?style=for-the-badge" alt="Live Demo"></a>
</p>
<p align="center">
  <img src="https://raw.githubusercontent.com/Moonlight12911/Django-URL-Shortener/main/assets/image.png" alt="Django URL Shortener">
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/Moonlight12911/Django-URL-Shortener/main/assets/image2.png" alt="Django URL Shortener Screenshot">
</p>
## ✨ Features

- **Long to Short URL Conversion**: Easily convert any valid URL into a compact, easily shareable short link.
- **Unique Link Generation**: Automatically ensures that all generated short codes are unique.
- **Instant Redirection**: Transparently redirects users from a short link to the original target destination.
- **Minimalistic Responsive UI**: Clean and straightforward interface for creating short links.
- **Admin Dashboard**: Built-in Django admin interface to manage and search shortened URLs.
- **Automated Test Suite**: Unit tests covering models, views, and redirection.

## 🛠️ Tech Stack

- **Backend**: Python, Django
- **Frontend**: HTML5, CSS3
- **Database**: SQLite
- **Deployment**: Gunicorn, WhiteNoise, Render

## 📁 Project Structure

```text
Django_URL_Shortener/
├── core/                               # Project configuration (settings, root URLs, WSGI)
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── docs/                               # Project documentation & specs (ignored in git)
│   └── django_url_shortener_documentation.pdf
├── shortener/                          # URL shortener application
│   ├── migrations/
│   │   ├── __init__.py
│   │   └── 0001_initial.py             # Database migrations
│   ├── __init__.py
│   ├── admin.py                        # ModelAdmin registrations
│   ├── apps.py                         # App configuration
│   ├── models.py                       # ShortURL model
│   ├── tests.py                        # Automated unit tests
│   ├── urls.py                         # App routing
│   └── views.py                        # Shortening & redirection logic
├── templates/                          # HTML templates
│   └── home.html                       # Landing page template
├── .gitignore                          # Git ignore rules
├── manage.py                           # Django CLI manager
├── README.md                           # Project documentation
└── requirements.txt                    # Python dependencies
```

## 🚀 Installation & Local Setup

### 1. Clone the repository
```bash
git clone https://github.com/Moonlight12911/Django-URL-Shortener.git
cd Django-URL-Shortener
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply migrations
```bash
python manage.py migrate
```

### 5. Run tests
```bash
python manage.py test
```

### 6. Start the development server
```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

## 📌 Usage

1. Open the homepage in your browser.
2. Enter the long URL you want to shorten into the input form.
3. Submit the form to generate your short URL.
4. Share the shortened link. Accessing it will seamlessly redirect to the original destination!

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to fork the repository and submit a pull request.

## 📄 License

This project is licensed under the **MIT License**.
