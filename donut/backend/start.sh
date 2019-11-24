#!/bin/sh
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --no-input
gunicorn config.wsgi -w 2 --bind 0.0.0.0:8000 --reload