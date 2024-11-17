from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Book
from .forms import BookSearchForm
from .forms import ExampleForm


@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    """
    View to display a list of all books.
    Requires the user to have the 'can_view' permission.
    """
    
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})


# Create your views here.
# View books
@permission_required('bookshelf.can_view', raise_exception=True)
def view_books(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/view_books.html', {'books': books})

# Create a book
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        Book.objects.create(title=title, author=author)
        return HttpResponse("Book created successfully!")
    return render(request, 'bookshelf/create_book.html')

# Edit a book
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.save()
        return HttpResponse("Book updated successfully!")
    return render(request, 'bookshelf/edit_book.html', {'book': book})

# Delete a book
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return HttpResponse("Book deleted successfully!")
    return render(request, 'bookshelf/delete_book.html', {'book': book})



def book_list(request):
    """
    View to list books. Handles user inputs safely to avoid SQL injection.
    """
    form = BookSearchForm(request.GET or None)  # Use a form to validate input
    books = Book.objects.all()

    if form.is_valid():  # Validate and sanitize input
        query = form.cleaned_data.get('search')
        if query:
            books = books.filter(title__icontains=query)  # Safe filtering

    return render(request, 'bookshelf/book_list.html', {'books': books, 'form': form})


def example_form_view(request):
    """
    View to handle the ExampleForm submission.
    """
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process the form data
            cleaned_data = form.cleaned_data
            name = cleaned_data.get('name')
            email = cleaned_data.get('email')
            message = cleaned_data.get('message')
            # Add processing logic here (e.g., save to database, send email, etc.)
            return render(request, 'bookshelf/form_success.html', {'name': name})
    else:
        form = ExampleForm()

    return render(request, 'bookshelf/form_example.html', {'form': form})
