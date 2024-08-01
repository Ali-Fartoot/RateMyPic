#!/bin/bash
python manage.py makemigrations
python manage.py migrate

python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('ali', '', 'Pol@ris01')"

python manage.py runserver 0.0.0.0:8000
