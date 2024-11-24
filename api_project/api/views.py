from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets

# Create your views here.

class BookList(generics.ListAPIView):
    """
    API view to list all books in the database.
    """
    queryset = Book.objects.all()  # Queryset to fetch all Book instances
    serializer_class = BookSerializer  # Serializer to convert data to JSON



class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions
    for the Book model (CRUD: Create, Read, Update, Delete).
    """
    queryset = Book.objects.all()  # Define the data to be managed
    serializer_class = BookSerializer  # Use the serializer to define data format
