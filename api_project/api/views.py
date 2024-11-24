from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer

# Create your views here.

class BookList(ListAPIView):
    """
    API view to list all books in the database.
    """
    queryset = Book.objects.all()  # Queryset to fetch all Book instances
    serializer_class = BookSerializer  # Serializer to convert data to JSON


# generics.ListAPIView