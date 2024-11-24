from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer

# Create your views here.

class BookList(ListAPIView):
    queryset = Book.objects.all()  # Queryset to fetch all Book instances
    serializer_class = BookSerializer  # Serializer to convert data to JSON
