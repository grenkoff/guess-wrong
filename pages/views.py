from django.shortcuts import render

from words.models import RealWord
from .models import HomePage


def home_view(request):
    home_page = HomePage.get_instance()
    random_word = RealWord.get_random_word()  # Получаем случайное слово

    return render(request, 'pages/home.html', {
        "is_home": True,
        'home_view': home_page,
        'random_word': random_word,  # Передаем случайное слово в шаблон
    })


def page_not_found(request, exception):
    return render(request, "pages/404.html", status=404)
