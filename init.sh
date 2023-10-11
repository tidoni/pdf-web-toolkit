#!/bin/bash

# (cd /app/ && gunicorn --access-logfile '-' --error-logfile '-' -w 4 -b 0.0.0.0:8000 wsgi:app) # Dev (Logging to console)
(cd /app/ && gunicorn -w 4 -b 0.0.0.0:8000 wsgi:app)

/bin/bash