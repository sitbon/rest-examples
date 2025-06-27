This is a new NextJS project. 

Code up a demo NextJS+Postgres example following best practices. 

The site will be called "foo-demo" or "Foo Demo". 

Use docker compose (with compose.yaml as the compose file) to set up dependent services like postgresql or redis. 

Keep track of your progress in CLAUDE.md and save regularly. 

Start by putting this prompt in there to remember your directive. 

Please keep working and do not stop until the work is done.

Think deeply.

## Progress Update

### Completed Tasks:
1. ✅ Set up Docker Compose with PostgreSQL
   - Created compose.yaml with PostgreSQL service
   - Added development and production app services
   - Configured health checks and networking

2. ✅ Created NextJS project structure and configuration
   - Set up TypeScript, Tailwind CSS, and ESLint
   - Created proper directory structure (src/app, components, lib)
   - Configured Next.js for standalone output

3. ✅ Set up database connection and ORM (Prisma)
   - Configured Prisma with PostgreSQL
   - Created database connection utility
   - Set up environment variables

4. ✅ Created database schema and models
   - User model with email, name, and timestamps
   - Post model with title, content, published status
   - Established relationships between models
   - Created seed data

5. ✅ Implemented REST API endpoints
   - Full CRUD operations for /api/users
   - Full CRUD operations for /api/posts
   - Query parameters support (e.g., ?published=true)

6. ✅ Added error handling and validation
   - Zod schemas for request validation
   - Proper error responses with status codes
   - Handling of unique constraints and not found errors

### Project Structure:
```
foo-demo/
├── src/
│   ├── app/
│   │   ├── api/
│   │   │   ├── users/
│   │   │   │   ├── route.ts
│   │   │   │   └── [id]/
│   │   │   │       └── route.ts
│   │   │   └── posts/
│   │   │       ├── route.ts
│   │   │       └── [id]/
│   │   │           └── route.ts
│   │   ├── layout.tsx
│   │   ├── page.tsx
│   │   └── globals.css
│   └── lib/
│       └── prisma.ts
├── prisma/
│   ├── schema.prisma
│   └── seed.ts
├── compose.yaml
├── dockerfile
├── package.json
├── tsconfig.json
├── tailwind.config.ts
├── next.config.mjs
└── README.md
```

### Next Steps:
- Run `docker compose up -d` to start the application
- Access the API at http://localhost:3000
- Test endpoints using curl, Postman, or any HTTP client

## Final Status: ✅ COMPLETE

The NextJS + PostgreSQL REST API demo is now fully functional with:
- Docker Compose setup running successfully
- PostgreSQL database configured and seeded with sample data
- All REST API endpoints working properly
- Full CRUD operations for Users and Posts
- Request validation with Zod
- Proper error handling

### Running the Application:
```bash
# Start the services
docker compose up -d

# Run database migrations (if needed)
npx prisma db push

# Seed the database
npx prisma db seed

# Check the application
curl http://localhost:3000/api/users
```

