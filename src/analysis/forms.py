from django import forms

class SentimentForm(forms.Form):
    user_input = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'Enter your text here...'}))