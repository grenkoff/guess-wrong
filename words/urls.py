from django.urls import path
from .views import wordlist_view, word_view

app_name = 'words'

urlpatterns = [
    path('', wordlist_view, name='wordlist'),
    path('<str:word>/', word_view, name='word_view'),
]
