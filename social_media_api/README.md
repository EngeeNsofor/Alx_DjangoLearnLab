# Social Media API

A **Django REST Framework**-based API for a social media platform. This project provides foundational features such as user authentication, registration, and profile management. It is designed as the starting point for building a complete social media application.

---

## Features

- **User Authentication**: Token-based authentication using Django REST Framework.
- **User Registration**: Endpoint to create new user accounts.
- **User Profile Management**: Customizable user profiles with fields for `bio`, `profile_picture`, and `followers`.
- **Secure Password Management**: Built using Django's authentication system.

---

## Setup Instructions

### Prerequisites

- Python 3.9 or later
- Django 4.x
- Django REST Framework 3.x
- pip (Python package installer)

### Installation Steps

1. **Clone the Repository**  
   Clone this project from GitHub to your local machine:
   ```bash
   git clone https://github.com/your-username/social_media_api.git
   cd social_media_api



## Follow and Unfollow Users

- **Follow User**
    - **Endpoint:** `POST /api/accounts/follow/<user_id>/`
    - **Description:** Allows the authenticated user to follow another user by their `user_id`.
    - **Request Body:** None
    - **Response Example:** 
      ```json
      {
        "detail": "You are now following username."
      }
      ```

- **Unfollow User**
    - **Endpoint:** `POST /api/accounts/unfollow/<user_id>/`
    - **Description:** Allows the authenticated user to unfollow another user by their `user_id`.
    - **Request Body:** None
    - **Response Example:** 
      ```json
      {
        "detail": "You have unfollowed username."
      }
      ```


## Feed

- **View Feed**
    - **Endpoint:** `GET /api/posts/feed/`
    - **Description:** Retrieves the posts from users that the authenticated user follows, ordered by the most recent posts.
    - **Response Example:** 
      ```json
      [
        {
          "id": 1,
          "title": "Post Title",
          "content": "This is a post content.",
          "author": "username",
          "created_at": "2024-12-15T12:00:00Z"
        },
        {
          "id": 2,
          "title": "Another Post Title",
          "content": "This is another post content.",
          "author": "another_username",
          "created_at": "2024-12-14T10:30:00Z"
        }
      ]
      ```

