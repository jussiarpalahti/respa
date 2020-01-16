#!/bin/bash

echo "NOTICE: Get static files for serving"
python3 ./manage.py collectstatic --no-input

echo "NOTICE: Start the uwsgi web server"
exec uwsgi --http :8000 --wsgi-file deploy/wsgi.py --check-static /usr/src/app/www --logto2 /logs/uwsgi.log -p 10 -T
