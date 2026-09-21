# Social Media Backend API

A backend-only **Social Media REST API** built using **Django and Django REST Framework (DRF)**.

This project provides the core backend functionality of a social media application, including **user authentication, profiles, posts, image uploads, likes, comments, follow/unfollow functionality, personalized feeds, search, filtering, pagination, and ordering**.

The API is deployed on **Render** and can be tested using **Postman**.

---

🚀 Live API

Base URL:

https://social-media-backend-ypng.onrender.com/

Swagger API Documentation:

https://social-media-backend-ypng.onrender.com/swagger/

You can use the deployed API with Postman or Swagger UI to test the available endpoints.

Note: This project is backend-only. There is currently no frontend interface.

---

# 📌 Project Overview

The Social Media Backend allows users to:

* Register and create an account
* Login using JWT authentication
* Access and update their profile
* Create posts
* Update and delete their own posts
* Upload images with posts
* Like and unlike posts
* Create, update and delete comments
* Follow and unfollow other users
* View posts from users they follow
* Search posts
* Order posts
* Navigate posts using pagination
* Access protected APIs using authentication and permissions

The project follows a **REST API architecture**, making it possible to connect the backend with a frontend application such as React in the future.

---

# 🛠️ Technologies Used

* **Python**
* **Django**
* **Django REST Framework**
* **Simple JWT**
* **PostgreSQL**
* **SQLite** (local development)
* **Pillow** – image handling
* **Git & GitHub**
* **Render** – deployment
* **Postman** – API testing

---

# 🧠 Concepts Used

This project demonstrates practical backend development concepts such as:

### Django

* Django Models
* Custom User Model
* `AbstractUser`
* Relationships between models
* `ForeignKey`
* `ManyToManyField`
* Django ORM
* Migrations
* Media files

### Django REST Framework

* APIViews
* Serializers
* Validation
* CRUD operations
* Permissions
* Authentication
* Pagination
* Search
* Ordering
* HTTP status codes
* Error handling

### Authentication & Security

* JWT Authentication
* Access Tokens
* Refresh Tokens
* Protected endpoints
* Password hashing
* Environment variables for sensitive configuration

### Database

* PostgreSQL
* SQLite for local development
* Relational database relationships
* Django ORM queries

### Deployment

* GitHub
* Render
* PostgreSQL on Render
* Environment variables
* Production deployment

---

# 📂 Main Features

## 1. User Registration

Users can create an account by providing required information such as username, email and password.

**Method:** `POST`

**Endpoint:**

```text
/api/v1/register/
```

### Example Request

```json
{
    "username": "pratham",
    "email": "pratham@example.com",
    "password": "password123"
}
```

A successful request creates a new user.

---

# 🔐 2. User Login

Users can login using their username and password.

The API uses **JWT authentication** and returns:

* Access Token
* Refresh Token

**Method:** `POST`

```text
/api/v1/login/
```

### Example Request

```json
{
    "username": "pratham",
    "password": "password123"
}
```

### Example Response

```json
{
    "refresh": "your_refresh_token",
    "access": "your_access_token"
}
```

The **access token** is then used to access protected endpoints.

In Postman:

```text
Authorization → Bearer Token → <access_token>
```

---

# 👤 3. User Profile

Authenticated users can access their profile information.

**Method:** `GET`

```text
/api/v1/profile/
```

This endpoint requires JWT authentication.

Use:

```text
Authorization: Bearer <access_token>
```

---

# 📝 4. Create a Post

Authenticated users can create posts.

A post can contain:

* Caption
* Image
* User/owner
* Creation time
* Updated time

**Method:** `POST`

```text
/api/v1/posts/
```

### Example

For a text-only post, use:

```text
Content-Type: application/json
```

```json
{
    "caption": "My first post!"
}
```

---

# 🖼️ 5. Image Upload

Posts can also contain images.

For image uploads, use:

```text
Content-Type: multipart/form-data
```

In Postman:

```text
Body → form-data
```

Add:

```text
caption → My new post
image → Select File
```

The backend uses **Pillow** for image handling.

Uploaded images are served through the configured media URL.

Example:

```text
/media/posts/example.jpg
```

---

# 📄 6. View Posts

Users can retrieve available posts.

**Method:** `GET`

```text
/api/v1/posts/
```

The API supports:

* Pagination
* Search
* Ordering

---

# ✏️ 7. Update a Post

Users can update their own posts.

**Method:** `PUT`

```text
/api/v1/posts/<post_id>/
```

Example:

```text
/api/v1/posts/1/
```

### Example Request

```json
{
    "caption": "Updated caption"
}
```

Only the owner of the post can update it.

---

# 🗑️ 8. Delete a Post

Users can delete their own posts.

**Method:** `DELETE`

```text
/api/v1/posts/<post_id>/
```

Example:

```text
/api/v1/posts/1/
```

The API uses permission checks to prevent other users from deleting someone else's post.

---

# ❤️ 9. Like a Post

Authenticated users can like a post.

**Method:** `POST`

```text
/api/v1/posts/<post_id>/like/
```

Example:

```text
/api/v1/posts/1/like/
```

The API prevents the same user from liking the same post multiple times.

---

# 💔 10. Unlike a Post

Users can remove their like from a post.

**Method:** `DELETE`

```text
/api/v1/posts/<post_id>/like/
```

Example:

```text
/api/v1/posts/1/like/
```

---

# 💬 11. Create a Comment

Authenticated users can comment on posts.

**Method:** `POST`

```text
/api/v1/posts/<post_id>/comments/
```

### Example Request

```json
{
    "text": "Nice post!"
}
```

---

# ✏️ 12. Update a Comment

Users can update their own comments.

**Method:** `PUT`

```text
/api/v1/comments/<comment_id>/
```

Example:

```text
/api/v1/comments/1/
```

---

# 🗑️ 13. Delete a Comment

Users can delete their own comments.

**Method:** `DELETE`

```text
/api/v1/comments/<comment_id>/
```

---

# 👥 14. Follow a User

Authenticated users can follow another user.

**Method:** `POST`

```text
/api/v1/users/<user_id>/follow/
```

Example:

```text
/api/v1/users/2/follow/
```

The API prevents:

* Following yourself
* Following the same user multiple times
* Following a non-existing user

---

# 🚫 15. Unfollow a User

Users can unfollow another user.

**Method:** `DELETE`

```text
/api/v1/users/<user_id>/follow/
```

Example:

```text
/api/v1/users/2/follow/
```

---

# 📰 16. User Feed

Authenticated users can view posts from users they follow.

**Method:** `GET`

```text
/api/v1/feed/
```

The feed is based on the user's following relationships.

For example:

```text
User A follows User B

User B creates:
- Post 1
- Post 2
- Post 3

User A's feed can display:
- Post 1
- Post 2
- Post 3
```

---

# 🔎 17. Search Posts

The API supports searching posts using the caption.

Example:

```text
/api/v1/posts/?search=python
```

The search functionality is implemented using DRF's:

```text
SearchFilter
```

Search field:

```python
search_fields = ['caption']
```

---

# ↕️ 18. Order Posts

Posts can be ordered using supported fields.

For example:

```text
/api/v1/posts/?ordering=created_at
```

Or:

```text
/api/v1/posts/?ordering=-created_at
```

The `-` sign represents descending order.

Supported ordering fields include:

```text
id
created_at
```

The API uses DRF's:

```text
OrderingFilter
```

---

# 📑 19. Pagination

The posts API supports pagination to avoid returning all posts at once.

Example:

```text
/api/v1/posts/?page=1
```

```text
/api/v1/posts/?page=2
```

The current pagination configuration returns a limited number of posts per page.

---

# 🔑 Authentication Flow

The basic flow for using the API is:

```text
1. Register
      ↓
2. Login
      ↓
3. Receive JWT Access Token
      ↓
4. Add Access Token to Postman
      ↓
5. Access protected APIs
      ↓
6. Create / Update / Delete / Like / Follow etc.
```

For protected endpoints, add:

```text
Authorization: Bearer <access_token>
```

---

# 📮 Testing with Postman

You can test the complete backend using **Postman**.

### Basic testing order

```text
Register
   ↓
Login
   ↓
Copy Access Token
   ↓
Add Bearer Token
   ↓
Create Post
   ↓
View Posts
   ↓
Like / Unlike
   ↓
Comment
   ↓
Follow / Unfollow
   ↓
View Feed
```

For image upload:

```text
Body → form-data → image → File
```

---

# 🔒 Permissions & Validation

The API includes permission and validation checks such as:

* Authentication required for protected APIs
* Users can update/delete their own posts
* Users can update/delete their own comments
* Users cannot follow themselves
* Users cannot duplicate follows
* Users cannot duplicate likes
* Invalid users/posts are handled with appropriate responses
* Required data is validated before processing requests

---

# 🗄️ Database

The project uses a relational database.

### Local Development

SQLite can be used during local development.

### Production

The deployed application uses **PostgreSQL**.

The database configuration is handled using environment variables rather than hardcoding sensitive credentials.

---

# 🌐 Deployment

The project is deployed using:

* **GitHub** – source code
* **Render** – backend hosting
* **PostgreSQL** – production database

Production configuration uses environment variables for sensitive information such as:

```text
SECRET_KEY
DATABASE_URL
DEBUG
```

Sensitive values are not stored directly in the source code.

---

# 📁 Core Models

The main application models include functionality for:

* Users
* Posts
* Comments
* Likes
* Following relationships

The project uses Django relationships such as:

```text
ForeignKey
ManyToManyField
```

to represent relationships between users, posts and interactions.

---

# 🔗 API Feature Summary

| Feature        | Method | Purpose                | Authentication |
| -------------- | ------ | ---------------------- | -------------- |
| Register       | POST   | Create account         | ❌              |
| Login          | POST   | Get JWT tokens         | ❌              |
| Profile        | GET    | View profile           | ✅              |
| Posts          | GET    | View posts             | Depends on API |
| Create Post    | POST   | Create a post          | ✅              |
| Update Post    | PUT    | Update own post        | ✅              |
| Delete Post    | DELETE | Delete own post        | ✅              |
| Image Upload   | POST   | Upload post image      | ✅              |
| Like           | POST   | Like a post            | ✅              |
| Unlike         | DELETE | Remove like            | ✅              |
| Create Comment | POST   | Add comment            | ✅              |
| Update Comment | PUT    | Update own comment     | ✅              |
| Delete Comment | DELETE | Delete own comment     | ✅              |
| Follow         | POST   | Follow user            | ✅              |
| Unfollow       | DELETE | Unfollow user          | ✅              |
| Search         | GET    | Search posts           | Depends on API |
| Ordering       | GET    | Sort posts             | Depends on API |
| Pagination     | GET    | Split posts into pages | Depends on API |

---

# 🎯 Project Purpose

This project was developed to gain practical experience in **Python backend development and REST API development** using Django and Django REST Framework.

It demonstrates how a backend can handle:

* Authentication
* Authorization
* Database relationships
* CRUD operations
* File uploads
* User interactions
* API validation
* Search and filtering
* Pagination
* Production deployment

The backend can be extended in the future with a frontend application, additional social features, notifications, messaging and other production-level functionality.

---

## 👨‍💻 Author

Pratham Bhokare

B.E. Computer Engineering

### Technologies

`Python` `Django` `DRF` `PostgreSQL` `JWT` `Git` `GitHub` `Render` `Postman`
