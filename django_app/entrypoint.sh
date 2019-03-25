#!/bin/sh

# Make app level migration files
python manage.py makemigrations api --settings=${DJANGO_ENVIRONMENT}
python manage.py makemigrations --settings=${DJANGO_ENVIRONMENT}

# Make database specific migrations
python manage.py migrate --settings=${DJANGO_ENVIRONMENT}
python manage.py migrate --settings=${DJANGO_ENVIRONMENT} --database tenant_db_1
python manage.py migrate --settings=${DJANGO_ENVIRONMENT} --database tenant_db_2

python manage.py collectstatic --clear --no-input --settings=${DJANGO_ENVIRONMENT}

# Run Redis
redis-server --daemonize yes

exec "$@"

