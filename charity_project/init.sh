#!/bin/bash

# Миграции базы данных
python manage.py migrate

# Создание суперпользователя
python manage.py createsuperuser --noinput --username admin --email admin@example.com

# Установка пароля
python manage.py shell <<EOF
from django.contrib.auth.models import User
user = User.objects.get(username='admin')
user.set_password('admin')
user.save()
EOF
