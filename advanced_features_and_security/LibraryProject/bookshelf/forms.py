from django import forms

class BookSearchForm(forms.Form):
    search = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={
        'placeholder': 'Search books...',
        'class': 'search-input'
    }))
