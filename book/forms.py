from django import forms
from book.models import Book


class BookForm(forms.ModelForm):
    submitted_by_email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'your.email@example.com'
        }),
        help_text='We will send you a confirmation when this book is saved.'
    )

    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'genre', 'isbn', 'publication_date']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter book title'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter author name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Write a short description...'}),
            'genre': forms.Select(attrs={'class': 'form-select'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 9780134685991', 'maxlength': '13'}),
            'publication_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }