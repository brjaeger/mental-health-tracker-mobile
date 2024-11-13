from django.urls import path
from main.views import create_mood_flutter

path('create-flutter/', create_mood_flutter, name='create_mood_flutter'),