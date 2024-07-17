#!/bin/bash

# Activate virtual environment
source /home/ubuntu/roulettech-assessment/venv/bin/activate

# Pull the latest code from the repository
cd /home/ubuntu/roulettech-assessment
git pull origin main

# Install any new dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Apply database migrations
python manage.py makemigrations
python manage.py migrate

# Restart Gunicorn and Nginx
sudo supervisorctl restart gunicorn
sudo systemctl restart nginx

echo "Deployment completed successfully."
