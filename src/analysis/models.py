from django.contrib.auth.models import User
from django.db import models

class SentimentHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link each record to a user
    user_input = models.TextField()
    sentiment = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.sentiment}"