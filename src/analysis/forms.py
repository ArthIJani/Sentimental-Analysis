from django import forms
from django.core.validators import FileExtensionValidator

class SentimentForm(forms.Form):
    user_input = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'Enter your text here...'}))


class FileUploadForm(forms.Form):
    file = forms.FileField(label="Upload CSV File", validators=[FileExtensionValidator(['csv'])])