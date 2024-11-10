from django.urls import path
from . import views
from .views import list_books, LibraryDetailView  # Import both views for URL routing
from django.contrib.auth import views as auth_views  # Import built-in views


urlpatterns = [
    # URL pattern for the function-based view to list all books
    path('books/', list_books, name='list_books'),

    # URL pattern for the class-based view to show library details
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]

urlpatterns = [
    # Built-in login and logout views
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    
    # Custom registration view
    path('register/', views.register, name='register'),
]