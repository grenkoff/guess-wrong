from django.http import HttpRequest

from .models import HomePage


def home_view(request):
    return {'home_view': HomePage.objects.first()}


def canonical_url(request: HttpRequest):
    """
    Контекстный процессор для генерации канонического URL с HTTPS
    """
    canonical_path = request.build_absolute_uri(request.path)
    # Принудительно заменить http:// на https://
    canonical_path = canonical_path.replace("http://", "https://", 1)
    return {
        'CANONICAL_URL': canonical_path
    }
