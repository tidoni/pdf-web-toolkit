#!/bin/bash

# (cd /app/ && pytest tests/test_pdf_util.py)
(cd /app/ && pytest -o log_cli=true)

# (cd /app/ && gunicorn -w 4 -b 0.0.0.0:8000 wsgi:app)
(cd /app/ && gunicorn --access-logfile '-' --error-logfile '-' -w 4 -b 0.0.0.0:8000 wsgi:app) # Dev (Logging to console)

/bin/bash