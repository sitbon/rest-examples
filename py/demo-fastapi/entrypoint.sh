#!/bin/bash

# Wait for postgres
echo "Waiting for PostgreSQL..."
while ! pg_isready -h db -p 5432 -U foo; do
    echo "PostgreSQL is unavailable - sleeping"
    sleep 1
done
echo "PostgreSQL is ready"

# Start the FastAPI app
echo "Starting FastAPI app..."
exec uvicorn main:app --host 0.0.0.0 --port 8000 --reload
