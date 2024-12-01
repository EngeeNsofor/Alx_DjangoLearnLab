from datetime import datetime
from django.shortcuts import render
from nbformat import ValidationError
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from .models import Book
from .serializers import BookSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

# List all books
class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]  # Read-only access for unauthenticated users

    # Enable filtering, searching, and ordering
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    # Define filterable fields
    filterset_fields = ['title', 'author__name', 'publication_year']

    # Define searchable fields
    search_fields = ['title', 'author__name']

    # Define ordering fields
    ordering_fields = ['title', 'publication_year']


# Retrieve a single book by ID
class BookDetailView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]  # Read-only access for unauthenticated users

# Create a new book
class BookCreateView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Only authenticated users can create and Read-only for unauthenticated users

    def perform_create(self, serializer):
        # Example of custom validation: publication_year cannot be in the future
        if serializer.validated_data['publication_year'] > datetime.date.today().year:
            raise ValidationError("Publication year cannot be in the future.")
        serializer.save()

# Update an existing book
class BookUpdateView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can update

# Delete a book
class BookDeleteView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can delete


class BookCreateView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Example of custom validation: publication_year cannot be in the future
        if serializer.validated_data['publication_year'] > datetime.date.today().year:
            raise ValidationError("Publication year cannot be in the future.")
        serializer.save()

