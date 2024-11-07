from django.shortcuts import render, get_object_or_404
from .models import RealWord, Example, Synonym, Antonym


def word_view(request, word):
    word_page = get_object_or_404(RealWord, word__iexact=word)  # игнорируем регистр при поиске

    examples = Example.objects.filter(word=word_page)

    # Проверяем наличие связанных RealWord для синонимов и антонимов с учетом регистра
    synonyms = [
        {
            'text': synonym.text,
            'exists': RealWord.objects.filter(word__iexact=synonym.text).exists()
        }
        for synonym in Synonym.objects.filter(word=word_page)
    ]

    antonyms = [
        {
            'text': antonym.text,
            'exists': RealWord.objects.filter(word__iexact=antonym.text).exists()
        }
        for antonym in Antonym.objects.filter(word=word_page)
    ]

    return render(request, 'words/word.html', {
        'word_page': word_page,
        'examples': examples,
        'synonyms': synonyms,
        'antonyms': antonyms,
    })
