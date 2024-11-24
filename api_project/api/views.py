from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.

# generics.ListAPIView
class BookList(ListAPIView):
    """
    API view to list all books in the database.
    """
    queryset = Book.objects.all()  # Queryset to fetch all Book instances
    serializer_class = BookSerializer  # Serializer to convert data to JSON



class BookViewSet(ModelViewSet):
    """
    A viewset that provides the standard actions
    for the Book model (CRUD: Create, Read, Update, Delete).
    """
    queryset = Book.objects.all()  # Define the data to be managed
    serializer_class = BookSerializer  # Use the serializer to define data format
