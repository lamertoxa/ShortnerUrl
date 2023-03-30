from django import forms
from django.core.validators import URLValidator

class ShortenURLForm(forms.Form):
    original_url = forms.CharField(
        validators=[URLValidator()],
        widget=forms.TextInput(attrs={'placeholder': 'Shorten your link here...'}),
        required=True
    )