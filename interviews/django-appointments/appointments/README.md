# Appointments Practice Test #

This is a sample test for generating Appointments and displaying existing appointments with python, django, ajax, jquery, json, and bootstrap

## Python ##
- 3.6.2

## Usage ##
- Clone the repo at $ git clone https://github.com/sabrown89/python-practice-problems.git
- Navigate to the django-appointments directory: $ cd python-practice-problems/interviews/django-appointments/appointments
- Create a new virtual environment if desired: $ python3 -m venv <virtualenv directory>
- Use pip to install all requirements in the requirements.txt file: $ pip install -r requirements.txt
- Create a .env file in the current directory (where manage.py is) with a variable named: DJANGO_SECRET_KEY='somesecretkey'
- Generate or place a secret key in the .env file
- run migrations: $ python manage.py migrate
- run the server: $ python manage.py runserver
- development server should be running at: localhost:8000
- The Search Field will fuzzy search characters in the 'description' field of the appointment
- Add a new a Appointment by clicking 'New', filling out all fields, and clicking 'Add'
- Close the new appointment form by clicking the 'Cancel' button if 'New' is clicked
