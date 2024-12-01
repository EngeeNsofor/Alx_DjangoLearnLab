# Advanced API Project

This project demonstrates how to use Django REST Framework (DRF) to build a robust API with CRUD functionality for managing books. It includes custom views, generic views, permissions, and endpoint documentation.

---

## **API Overview**

The API provides endpoints to perform CRUD (Create, Read, Update, Delete) operations on the `Book` model, which includes fields like `title`, `publication_year`, and `author`. Below is a detailed list of available endpoints:

### **Endpoints**

| Endpoint                  | HTTP Method | Description              | Permissions       |
|---------------------------|-------------|--------------------------|-------------------|
| `/api/books/`             | GET         | List all books           | Public (read-only)|
| `/api/books/<id>/`        | GET         | Retrieve a single book   | Public (read-only)|
| `/api/books/create/`      | POST        | Create a new book        | Authenticated     |
| `/api/books/<id>/update/` | PUT         | Update an existing book  | Authenticated     |
| `/api/books/<id>/delete/` | DELETE      | Delete a book            | Authenticated     |

---

## **Setup Instructions**

Follow these steps to set up the project locally:

### **1. Clone the Repository**
```bash
git clone <repository-url>
cd advanced_api_project
