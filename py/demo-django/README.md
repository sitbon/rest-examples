# Django REST API Demo

A Django REST Framework project demonstrating a simple API setup.

## Getting Started

### 1. Start Database Container

Start the PostgreSQL database using Docker Compose:

```bash
docker compose up -d
```

This will start a PostgreSQL container configured for the project.

### 2. Run Server in Development Mode

First, ensure you have the dependencies installed:

```bash
pip install -r requirements.txt
```

Run database migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

The server will be available at `http://localhost:8000/`

### 3. Generate OpenAPI Schema

To generate the OpenAPI schema for the API:

```bash
python manage.py generateschema > schema.yaml
```

This will create a `schema.yaml` file containing the OpenAPI specification for your API endpoints.