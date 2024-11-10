from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from django.views.generic.detail import DetailView
from .models import Library
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from .models import UserProfile
from .forms import BookForm  # Assuming you have a BookForm for creating/editing books

# Create your views here.

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # Query all books
    return render(request, 'relationship_app/list_books.html', {'books': books})


# Class-based view to show library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


# Custom registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after registration
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserCreationForm()  # Display the empty form
    
    return render(request, 'relationship_app/register.html', {'form': form})


@login_required
def some_view(request):
    # This view will only be accessible to logged-in users
    return render(request, 'some_template.html')


# Check if user is an Admin
def is_admin(user):
    return user.userprofile.role == 'Admin'

# Check if user is a Librarian
def is_librarian(user):
    return user.userprofile.role == 'Librarian'

# Check if user is a Member
def is_member(user):
    return user.userprofile.role == 'Member'

# Admin view (only accessible to Admin users)
@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# Librarian view (only accessible to Librarian users)
@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# Member view (only accessible to Member users)
@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')


# Add a new book (only users with 'can_add_book' permission)
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Redirect to book list after adding
    else:
        form = BookForm()

    return render(request, 'relationship_app/book_form.html', {'form': form})

# Edit an existing book (only users with 'can_change_book' permission)
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Redirect to book list after editing
    else:
        form = BookForm(instance=book)

    return render(request, 'relationship_app/book_form.html', {'form': form})

# Delete a book (only users with 'can_delete_book' permission)
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')  # Redirect to book list after deletion

    return render(request, 'relationship_app/book_confirm_delete.html', {'book': book})