# FastAPI + SQLAlchemy + Pydantic Settings + Docker Compose Example

## Project: Foo Demo

This is a demo FastAPI project using SQLAlchemy, asyncpg, Alembic, and pydantic-settings, with Docker Compose for local development. It provides a simple user CRUD and API.

### Features
- FastAPI app with async SQLAlchemy and PostgreSQL
- Redis service for future caching/queueing
- Pydantic-settings for configuration
- Alembic for database migrations
- Docker Compose for local development
- Hot-reload enabled for development
- Modern Python dependency management with `uv`

## Running the Application

### Prerequisites
- Docker and Docker Compose installed
- Port 8000, 5432, and 6379 available

### Quick Start

1. **Start all services:**
   ```bash
   docker compose up --build
   ```
   This will:
   - Build the FastAPI application container
   - Start PostgreSQL database (port 5432)
   - Start Redis cache (port 6379)
   - Start the FastAPI app (port 8000)

2. **Access the application:**
   - API: http://localhost:8000
   - Interactive API docs: http://localhost:8000/docs
   - ReDoc documentation: http://localhost:8000/redoc

3. **Stop services:**
   ```bash
   docker compose down
   ```
   Add `-v` to also remove volumes (database data):
   ```bash
   docker compose down -v
   ```

### Development Mode
The application runs with hot-reload enabled. Any changes to Python files will automatically restart the server.

## Application Structure

```
demo-fastapi/
├── app/                    # Main application package
│   ├── __init__.py
│   ├── crud.py            # Database operations (Create, Read, Update, Delete)
│   ├── db.py              # Database configuration and session management
│   ├── models.py          # SQLAlchemy ORM models
│   ├── schemas.py         # Pydantic models for request/response validation
│   ├── settings.py        # Application configuration
│   └── routers/           # API route handlers
│       └── users.py       # User endpoints
├── alembic/               # Database migrations
│   ├── env.py            # Alembic environment configuration
│   ├── models.py         # Model imports for migrations
│   └── versions/         # Migration files
├── main.py               # FastAPI application entry point
├── alembic.ini           # Alembic configuration
├── compose.yaml          # Docker Compose configuration
├── dockerfile            # Docker image definition
├── entrypoint.sh         # Container startup script
├── pyproject.toml        # Python dependencies (using uv)
└── uv.lock              # Locked dependencies

```

### Key Components

- **FastAPI App (`main.py`)**: Application initialization and route inclusion
- **Models (`app/models.py`)**: SQLAlchemy ORM models defining database schema
- **Schemas (`app/schemas.py`)**: Pydantic models for API validation
- **CRUD (`app/crud.py`)**: Async database operations
- **Settings (`app/settings.py`)**: Environment-based configuration using pydantic-settings
- **Database (`app/db.py`)**: Async SQLAlchemy engine and session management

## Database Migrations with Alembic

### Understanding Alembic
Alembic is a database migration tool for SQLAlchemy. It tracks changes to your database schema over time and applies them incrementally.

### Running Migrations

1. **Apply all migrations (automatic on startup):**
   The entrypoint script automatically runs migrations when the container starts.

2. **Manual migration commands:**
   ```bash
   # Enter the app container
   docker compose exec app bash
   
   # Check current migration status
   uv run alembic current
   
   # Apply all pending migrations
   uv run alembic upgrade head
   
   # Rollback one migration
   uv run alembic downgrade -1
   ```

### Creating New Migrations

When you modify models in `app/models.py`:

1. **Generate a new migration:**
   ```bash
   docker compose exec app uv run alembic revision --autogenerate -m "Description of changes"
   ```
   This will:
   - Compare current database schema with models
   - Generate a migration file in `alembic/versions/`
   - Include upgrade and downgrade functions

2. **Review the generated migration:**
   Always check the generated file to ensure it correctly represents your intended changes.

3. **Apply the migration:**
   ```bash
   docker compose exec app uv run alembic upgrade head
   ```

### Migration Best Practices

- Always review auto-generated migrations before applying
- Use descriptive messages for migrations
- Test both upgrade and downgrade paths
- Never edit existing migrations that have been applied to production

## API Endpoints

### Users API

- **GET `/`** - Welcome message and health check
- **GET `/health`** - Health check endpoint
- **POST `/users/`** - Create a new user
  ```json
  {
    "name": "John Doe",
    "email": "john@example.com",
    "description": "A sample user"
  }
  ```
- **GET `/users/`** - List all users (with pagination)
  - Query params: `skip` (default: 0), `limit` (default: 100)

## Configuration

The application uses environment variables for configuration:

- `DATABASE_URL`: PostgreSQL connection string (default: `postgresql+asyncpg://foo:foo@db:5432/foodb`)
- `REDIS_URL`: Redis connection string (default: `redis://redis:6379/0`)

These are automatically set in the Docker Compose environment.

## Development Tips

1. **View logs:**
   ```bash
   docker compose logs -f app
   ```

2. **Access PostgreSQL:**
   ```bash
   docker compose exec db psql -U foo -d foodb
   ```

3. **Access Redis:**
   ```bash
   docker compose exec redis redis-cli
   ```

4. **Run tests (when implemented):**
   ```bash
   docker compose exec app uv run pytest
   ```

### Progress
See `local/progress.md` for ongoing progress and notes.
