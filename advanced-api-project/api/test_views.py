from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Book, Author

class BookApiTests(APITestCase):
    
    def setUp(self):
        # Create a user for authentication purposes
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        
        # Create an author
        self.author = Author.objects.create(name="Test Author")
        
        # Create a book instance
        self.book = Book.objects.create(
            title="Test Book", 
            publication_year=2020, 
            author=self.author
        )
        
        # Authenticate the user
        self.client.login(username="testuser", password="testpassword")
        
    def test_create_book(self):
        # Test creating a new book
        url = "/api/books/"
        data = {
            "title": "New Book",
            "publication_year": 2021,
            "author": self.author.id
        }
        response = self.client.post(url, data, format="json")
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.latest('id').title, "New Book")

    def test_read_books(self):
        # Test fetching the list of books
        url = "/api/books/"
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Only one book in the database initially
        self.assertEqual(response.data[0]["title"], self.book.title)

    def test_update_book(self):
        # Test updating an existing book
        url = f"/api/books/{self.book.id}/"
        data = {"title": "Updated Book Title"}
        response = self.client.put(url, data, format="json")
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Book Title")
        
    def test_delete_book(self):
        # Test deleting a book
        url = f"/api/books/{self.book.id}/"
        response = self.client.delete(url)
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)
        
    def test_filter_books_by_author(self):
        # Test filtering books by author
        url = "/api/books/?author__name=Test Author"
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # We have one book by "Test Author"
        
    def test_search_books(self):
        # Test searching books by title
        url = "/api/books/?search=Test Book"
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], self.book.title)

    def test_order_books(self):
        # Test ordering books by title
        Book.objects.create(title="A Book", publication_year=2021, author=self.author)
        url = "/api/books/?ordering=title"
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "A Book")
        
    def test_permissions(self):
        # Test if permission works, user should not be able to create a book without login
        self.client.logout()  # Log out user
        url = "/api/books/"
        data = {
            "title": "Another Book",
            "publication_year": 2022,
            "author": self.author.id
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  # Forbidden because not logged in
