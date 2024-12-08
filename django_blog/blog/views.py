from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from .forms import UserForm, ProfileForm
from .models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post


# Create your views here.

def home(request):
    return render(request, 'blog/base.html')


class RegisterView(CreateView):
    template_name = "blog/register.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("login")


@login_required
def profile_view(request):
    if request.method == "POST":
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = UserChangeForm(instance=request.user)
    return render(request, "blog/profile.html", {"form": form})


@login_required
def profile_view(request):
    user = request.user
    profile, created = Profile.objects.get_or_create(user=user)

    if request.method == "POST":
        user_form = UserForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("profile")
    else:
        user_form = UserForm(instance=user)
        profile_form = ProfileForm(instance=profile)

    return render(
        request,
        "blog/profile.html",
        {"user_form": user_form, "profile_form": profile_form},
    )


# List all posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

# Show details of a single post
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

# Create a new post (authenticated users only)
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# Update a post (only for the post author)
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'
    context_object_name = 'post'
    success_url = reverse_lazy('post_list')

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)

# Delete a post (only for the post author)
class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)
