from django import forms
from .models import SentimentEntry

class SentimentForm(forms.ModelForm):
    class Meta:
        model = SentimentEntry
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'rows': 5,
                'cols': 50,
                'placeholder': 'Type your sentence here...'
            }),
        }