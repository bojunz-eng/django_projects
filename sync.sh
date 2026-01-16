#!/bin/bash

cd django_projects

git pull origin main

cd mysite
python manage.py check
