from django.shortcuts import render
from .models import HomePage


def home_view(request):
    home_page = HomePage.get_instance()
    return render(request, 'pages/home.html', {
        "is_home": True,
        'home_view': home_page,
    })


def page_not_found(request, exception):
    return render(request, "pages/404.html", status=404)
