from django.urls import path
from .views import word_view, puzzle_view

app_name = 'puzzle'

urlpatterns = [
    path('english/words/<str:word>', word_view, name='word'),
    path('', puzzle_view, name='puzzle'),
]
