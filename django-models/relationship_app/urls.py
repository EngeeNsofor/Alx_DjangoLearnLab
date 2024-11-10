from django.urls import path
from . import views
from .views import list_books, LibraryDetailView  # Import both views for URL routing


urlpatterns = [
    # URL pattern for the function-based view to list all books
    path('books/', list_books, name='list_books'),

    # URL pattern for the class-based view to show library details
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
