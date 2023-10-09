#!/bin/bash

echo "DEPLOYMENT_MODE is: '$DEPLOYMENT_MODE'"

# Build tailwindcss
tailwindcss -i ./flask_app/static/src/main.css -o ./flask_app/static/dist/main.css --minify

echo "TailwindCSS build complete."

# Determine whether to run in development or production mode
case "$DEPLOYMENT_MODE" in
prod)
    echo "Starting Gunicorn server..."
    gunicorn -b 0.0.0.0:8000 -w 5 'flask_app:create_app()'
    ;;
*)
    echo "Starting Flask development server..."
    python run.py
    ;;
esac



