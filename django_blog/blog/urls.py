from django.urls import path
from . import views
from .views import RegisterView, profile_view
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', views.home, name='home'),
    path("login/", LoginView.as_view(template_name="blog/login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path("profile/", profile_view, name="profile"),
]
