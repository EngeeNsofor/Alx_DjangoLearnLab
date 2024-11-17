from django import forms

class BookSearchForm(forms.Form):
    search = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={
        'placeholder': 'Search books...',
        'class': 'search-input'
    }))



class ExampleForm(forms.Form):
    """
    Example form for demonstration purposes.
    """
    name = forms.CharField(max_length=100, required=True, label='Name')
    email = forms.EmailField(required=True, label='Email Address')
    message = forms.CharField(widget=forms.Textarea, required=True, label='Message')

    def clean_name(self):
        """
        Custom validation for the 'name' field.
        """
        name = self.cleaned_data.get('name')
        if len(name) < 3:
            raise forms.ValidationError("Name must be at least 3 characters long.")
        return name

    def clean(self):
        """
        Custom form-wide validation.
        """
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        message = cleaned_data.get('message')

        if email and message and 'example.com' not in email:
            raise forms.ValidationError("Please use an email address from example.com.")

        return cleaned_data
