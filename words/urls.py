from django.urls import path
from .views import word_view

app_name = 'words'

urlpatterns = [
    path('<str:word>/', word_view, name='word_view'),
]
