# Foo Demo - NextJS + PostgreSQL REST API

A demonstration REST API built with NextJS 15 and PostgreSQL, featuring full CRUD operations for users and posts.

## Features

- NextJS 15 with App Router
- PostgreSQL database with Prisma ORM
- RESTful API endpoints for Users and Posts
- Docker Compose for easy setup
- TypeScript for type safety
- Zod for request validation
- Tailwind CSS for styling

## Prerequisites

- Docker and Docker Compose
- Node.js 20+ (for local development)
- npm or yarn

## Quick Start

1. Clone the repository and navigate to the project directory

2. Copy the environment variables:
   ```bash
   cp .env.example .env
   ```

3. Start the application with Docker Compose:
   ```bash
   docker compose up -d
   ```

4. The application will be available at http://localhost:3000

## Development

For local development without Docker:

1. Install dependencies:
   ```bash
   npm install
   ```

2. Set up the database:
   ```bash
   npm run db:push
   npm run db:seed
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```

## API Endpoints

### Users
- `GET /api/users` - List all users
- `GET /api/users/:id` - Get user by ID
- `POST /api/users` - Create new user
- `PUT /api/users/:id` - Update user
- `DELETE /api/users/:id` - Delete user

### Posts
- `GET /api/posts` - List all posts
- `GET /api/posts?published=true` - List published posts only
- `GET /api/posts/:id` - Get post by ID
- `POST /api/posts` - Create new post
- `PUT /api/posts/:id` - Update post
- `DELETE /api/posts/:id` - Delete post

## Database Management

- `npm run db:push` - Push schema changes to database
- `npm run db:migrate` - Create and run migrations
- `npm run db:seed` - Seed the database with sample data
- `npm run db:studio` - Open Prisma Studio for database management

## Docker Commands

- `docker compose up -d` - Start all services in detached mode
- `docker compose down` - Stop all services
- `docker compose logs -f app` - View application logs
- `docker compose exec app npm run db:seed` - Run database seeding in container