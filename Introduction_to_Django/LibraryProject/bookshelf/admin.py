from django.contrib import admin
from .models import Book

@admin.register(Book) # Registers the book model
class BookAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('title', 'author', 'publication_year')

    # Enable search functionality for title and author fields
    search_fields = ('title', 'author')

    # Add filters for publication year
    list_filter = ('publication_year',)