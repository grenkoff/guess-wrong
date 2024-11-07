from django.urls import path
from .views import play_view

app_name = 'play'

urlpatterns = [
    path('', play_view, name='play'),
]
