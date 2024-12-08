from django import forms
from django.contrib.auth.models import User
from .models import Profile
from .models import Post
from .models import Comment
from taggit.forms import TagWidget
from django.forms import widgets


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["bio", "profile_picture"]


class PostForm(forms.ModelForm):

    tags = forms.CharField(widget=TagWidget())

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags', 'widgets']

    content = forms.CharField(
        widget=widgets.Textarea(attrs={'cols': 80, 'rows': 20, 'placeholder': 'Write your post content here...'}),
        required=True
    )
    title = forms.CharField(
        widget=widgets.TextInput(attrs={'placeholder': 'Enter the title of your post'}),
        required=True
    )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']  # Only allow users to input the content of their comment

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Add a comment'})
