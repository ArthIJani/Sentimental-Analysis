from django.contrib import admin
from .models import SentimentHistory

@admin.register(SentimentHistory)
class SentimentHistoryAdmin(admin.ModelAdmin):
    list_display = ('user_input', 'sentiment', 'timestamp')  # Fields to display in the admin list view
    search_fields = ('user_input', 'sentiment')  # Add search functionality for these fields
    list_filter = ('sentiment', 'timestamp')  # Add filters for sentiment and date
    ordering = ('-timestamp',)  # Order records by timestamp, most recent first