from django.urls import path
from . import views
from .views import RegisterView, profile_view
from django.contrib.auth.views import LoginView, LogoutView
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, CommentUpdateView, CommentDeleteView


urlpatterns = [
    path('', views.home, name='home'),
    path("login/", LoginView.as_view(template_name="blog/login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path("profile/", profile_view, name="profile"),
    path('post/', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('comments/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment_edit'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
]

