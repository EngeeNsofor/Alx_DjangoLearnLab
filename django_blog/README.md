## Blog Post Management

This feature enables users to create, read, update, and delete blog posts. 

- **List**: View all posts at `/posts/`.
- **Create**: Authenticated users can create new posts at `/posts/new/`.
- **Read**: View individual post details at `/posts/<int:pk>/`.
- **Update**: Only the post author can edit posts at `/posts/<int:pk>/edit/`.
- **Delete**: Only the post author can delete posts at `/posts/<int:pk>/delete/`.
