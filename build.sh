#!/usr/bin/env bash
# exit on error
set -o errexit

# poetry install
pip install -r requirements.txt
pip install pywin32==302
pip install --upgrade pip

python manage.py collectstatic --no-input
python manage.py migrate