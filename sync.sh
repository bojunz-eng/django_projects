#!/bin/bash

cd django_projects

git pull origin main

cd market

mv -f config/settings_local.py config/settings.py

python manage.py makemigrations
python manage.py migrate
python manage.py check


