from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),          # GET: List all books
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),  # GET: Retrieve book by ID
    path('books/create/', BookCreateView.as_view(), name='book-create'),   # POST: Create a new book
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),  # PUT: Update a book
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),  # DELETE: Remove a book
]

"""
urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),          # GET: List all books
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),  # GET: Retrieve book by ID
    path('books/create/', BookCreateView.as_view(), name='book-create'),   # POST: Create a new book
    path('books/update/', BookUpdateView.as_view(), name='book-update'),  # PUT: Update a book
    path('books/delete/', BookDeleteView.as_view(), name='book-delete'),  # DELETE: Remove a book
]
"""