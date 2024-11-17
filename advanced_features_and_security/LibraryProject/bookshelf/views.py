from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Book


# Create your views here.
# View books
@permission_required('relationship_app.can_view', raise_exception=True)
def view_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/view_books.html', {'books': books})

# Create a book
@permission_required('relationship_app.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        Book.objects.create(title=title, author=author)
        return HttpResponse("Book created successfully!")
    return render(request, 'relationship_app/create_book.html')

# Edit a book
@permission_required('relationship_app.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.save()
        return HttpResponse("Book updated successfully!")
    return render(request, 'relationship_app/edit_book.html', {'book': book})

# Delete a book
@permission_required('relationship_app.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return HttpResponse("Book deleted successfully!")
    return render(request, 'relationship_app/delete_book.html', {'book': book})
