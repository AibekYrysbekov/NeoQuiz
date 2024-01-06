# NeoQuiz Project

NeoQuiz is a learning management system that allows users to access articles and quizzes for learning purposes.

## Description

The NeoQuiz project is developed to create a modern and user-friendly learning environment. It provides access to diverse articles and quizzes, allowing users to conveniently study materials and test their knowledge.

## Technologies

The project is built using the following technologies:
- Django - a Python web framework.
- Django REST Framework - a toolkit for building RESTful APIs in Django.
- PostgreSQL - a relational database management system.

## Installation and Setup

1. Ensure you have Python X.X or later installed.
2. Clone the repository: `git clone https://github.com/AibekYrysbekov/NeoQuiz.git`
3. Navigate to the project directory: `cd NeoQuiz`
4. Create a virtual environment: `python -m venv venv`
5. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS and Linux: `source venv/bin/activate`
6. Install dependencies: `pip install -r requirements.txt`
7. Configure the database in the `settings.py` file.
8. Create a `.env` file and specify necessary environment variables (e.g., `SECRET_KEY`, `DEBUG`, `DATABASE_URL`, etc.).
9. Apply migrations: `python manage.py migrate`
10. Run the server: `python manage.py runserver`

## Using the API

### Articles

- Get a list of all articles: `GET /articles/`
- Get an article by ID: `GET /articles/{article_id}/`
- Create a new article: `POST /articles/`
- ...

### Quizzes

- Get a list of all quizzes: `GET /quizzes/`
- Get a quiz by ID: `GET /quizzes/{quiz_id}/`
- Create a new quiz: `POST /quizzes/`
- ...

## .env File

The `.env` file is used to store sensitive or environment-specific variables such as:
- `SECRET_KEY`: Django project's secret key.
- `DEBUG`: Debug mode (True/False).
- `DATABASE_URL`: URL for connecting to the database.
- ...

## Author

- Author  - [@Aibek Yrysbekov](https://github.com/AibekYrysbekov)

