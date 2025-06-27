export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24">
      <div className="text-center max-w-4xl">
        <h1 className="text-4xl font-bold mb-4">Foo Demo</h1>
        <p className="text-xl text-gray-600">NextJS + PostgreSQL REST API</p>
        
        <div className="mt-8 grid grid-cols-1 md:grid-cols-2 gap-8 text-left">
          <div>
            <h2 className="text-2xl font-semibold mb-4">User Endpoints</h2>
            <ul className="space-y-2">
              <li><code className="bg-gray-100 px-2 py-1 rounded text-sm">GET /api/users</code> - List all users</li>
              <li><code className="bg-gray-100 px-2 py-1 rounded text-sm">GET /api/users/:id</code> - Get user by ID</li>
              <li><code className="bg-gray-100 px-2 py-1 rounded text-sm">POST /api/users</code> - Create new user</li>
              <li><code className="bg-gray-100 px-2 py-1 rounded text-sm">PUT /api/users/:id</code> - Update user</li>
              <li><code className="bg-gray-100 px-2 py-1 rounded text-sm">DELETE /api/users/:id</code> - Delete user</li>
            </ul>
          </div>
          
          <div>
            <h2 className="text-2xl font-semibold mb-4">Post Endpoints</h2>
            <ul className="space-y-2">
              <li><code className="bg-gray-100 px-2 py-1 rounded text-sm">GET /api/posts</code> - List all posts</li>
              <li><code className="bg-gray-100 px-2 py-1 rounded text-sm">GET /api/posts?published=true</code> - List published posts</li>
              <li><code className="bg-gray-100 px-2 py-1 rounded text-sm">GET /api/posts/:id</code> - Get post by ID</li>
              <li><code className="bg-gray-100 px-2 py-1 rounded text-sm">POST /api/posts</code> - Create new post</li>
              <li><code className="bg-gray-100 px-2 py-1 rounded text-sm">PUT /api/posts/:id</code> - Update post</li>
              <li><code className="bg-gray-100 px-2 py-1 rounded text-sm">DELETE /api/posts/:id</code> - Delete post</li>
            </ul>
          </div>
        </div>
      </div>
    </main>
  )
}