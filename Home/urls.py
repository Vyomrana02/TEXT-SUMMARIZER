from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('index', views.home, name='home'),
    path('GenerateSummary', views.GenerateSummary, name='GenerateSummary'),
    path('GenerateAudioSummary', views.GenerateAudioSummary,
         name='GenerateAudioSummary'),
]
