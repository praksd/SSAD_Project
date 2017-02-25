#!/bin/bash
cd Source
virtualenv env
source env/bin/activate

python manage.py runserver
