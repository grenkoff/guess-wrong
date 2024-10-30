from .models import HomePage

def home_view(request):
    return {'home_view': HomePage.objects.first()}
