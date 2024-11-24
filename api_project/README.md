## API Authentication
- Use `/api-token-auth/` to retrieve a token by posting `username` and `password`.
- Include the token in the `Authorization` header of subsequent requests:
- Endpoints are secured using `IsAuthenticated` by default.
- For modifying data, users must have admin privileges (`IsAdminOrReadOnly`).
