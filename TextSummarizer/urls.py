from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('Text-Summarizer', views.TextSummarize, name='TextSummarize'),
]
