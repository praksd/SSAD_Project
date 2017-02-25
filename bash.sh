#!/bin/bash
cd Source
virtualenv env
source env/bin/activate
pip freeze > requirements.txt
while read line; do 
pip install $line
done < requirements.txt
celery multi start w1 -B  -A pressp -l info
celery multi start w1 beat pressp -l info
python manage.py runserver
