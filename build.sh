#!/usr/bin/env bash

set -o errexit # Exit on error

pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate
python manage.py createsu 