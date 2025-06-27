# FastAPI + SQLAlchemy + Pydantic Settings + Docker Compose Example

## Project: Foo Demo

This is a demo FastAPI project using SQLAlchemy, asyncpg, Alembic, and pydantic-settings, with Docker Compose for local development. It provides a simple user CRUD API and is ready for interview live-coding.

### Features
- FastAPI app with async SQLAlchemy and PostgreSQL
- Redis service for future caching/queueing
- Pydantic-settings for configuration
- Alembic for migrations
- Docker Compose for local dev

### Usage

- `docker compose up --build` to start all services
- API available at http://localhost:8000
- Default DB: `postgresql+asyncpg://foo:foo@localhost:5432/foodb`

### Endpoints
- `GET /` - Welcome
- `POST /users/` - Create user
- `GET /users/` - List users

### Progress
See `local/progress.md` for ongoing progress and notes.
