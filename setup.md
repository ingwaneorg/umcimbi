# Setup instructions

## Summary

### Names
- Repository is called: umcimbi
- Project is called: event
- First app is called: tracker

### Components
- Written in Python 3.8.10 using Django 4.2
- Django uses SQLite (for development)
- PostgreSQL is used in Google Cloud

---
## Models

### Event
- id
- course/code --> FK
- active

### Courses
- code
- name

### Activities
- course/code --> FK
- day
- sort_order
- description

---
## Installation

### Install Django
- `pip install django`

### Create a Django Project
- `django-admin startproject event .`

### Check if everything works by running:
- `python manage.py runserver`
- This starts the development server at http://127.0.0.1:8000/
- You should see the Django welcome page

### Create a Django App
- `python manage.py startapp tracker`
- Creates a new app named **tracker** where we’ll add models, views, and templates.

### Register the App in Django
- Open `event/settings.py` and add 'tracker' to `INSTALLED_APPS:`

### Set Up the Database
- `python manage.py migrate`

### Create admin user
- `python manage.py createsuperuser`

---
## Ongoing

### After changing a model - run:
- `python manage.py makemigrations tracker`
- `python manage.py migrate`
- Add the details to admin: tracker / admin ~ (if required)


### to flush data - run:
- `python ??`
- Note: this deletes **all the users** as well!
- `python src/load_csv_data.py`
