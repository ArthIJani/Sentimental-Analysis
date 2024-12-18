from django.contrib.auth.models import User
from django.db import models
from django.core.validators import FileExtensionValidator

from transformers import pipeline
summarizer = pipeline("summarization")

class SentimentHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link each record to a user
    user_input = models.TextField()
    sentiment = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.sentiment}"


class UploadedFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/', validators=[FileExtensionValidator(['csv'])])
    uploaded_at = models.DateTimeField(auto_now_add=True)


def summarize_text(text):
    if len(text.split()) < 30:  # Ensure text has enough words to summarize
        return "Text is too short to summarize."
    summary = summarizer(text, max_length=50, min_length=25, do_sample=False)
    return summary[0]['summary_text']