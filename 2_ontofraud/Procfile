# Start application
web: gunicorn project.wsgi:application

# Apply migrations
release: python manage.py migrate --noinput
