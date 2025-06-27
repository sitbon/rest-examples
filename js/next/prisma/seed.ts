import { PrismaClient } from '@prisma/client'

const prisma = new PrismaClient()

async function main() {
  // Clean existing data
  await prisma.post.deleteMany()
  await prisma.user.deleteMany()

  // Create users
  const alice = await prisma.user.create({
    data: {
      email: 'alice@example.com',
      name: 'Alice Johnson',
      posts: {
        create: [
          {
            title: 'Getting Started with NextJS',
            content: 'NextJS is a powerful React framework...',
            published: true,
          },
          {
            title: 'Prisma Best Practices',
            content: 'When working with Prisma, consider these tips...',
            published: false,
          },
        ],
      },
    },
  })

  const bob = await prisma.user.create({
    data: {
      email: 'bob@example.com',
      name: 'Bob Smith',
      posts: {
        create: [
          {
            title: 'REST API Design Principles',
            content: 'Building RESTful APIs requires careful planning...',
            published: true,
          },
        ],
      },
    },
  })

  console.log('Seed data created:', { alice, bob })
}

main()
  .then(async () => {
    await prisma.$disconnect()
  })
  .catch(async (e) => {
    console.error(e)
    await prisma.$disconnect()
    process.exit(1)
  })