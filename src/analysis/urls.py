from django.urls import path
from . import views

urlpatterns = [
    path('', views.analyze_view, name='analyze'),
    path('batch/', views.batch_analysis_view, name='batch_analysis'),
    path('summarize/', views.summarize_view, name='summarize'),
]