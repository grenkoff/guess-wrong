from django.urls import path
from .views import puzzle_view

app_name = 'puzzle'

urlpatterns = [
    path('', puzzle_view, name='puzzle'),
]
