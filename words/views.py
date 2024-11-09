import os
import json

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from .models import RealWord, Example, Synonym, Antonym
from .serializers import RealWordSerializer


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


# def wordlist_view(request):
#     words = RealWord.objects.all()  # Retrieve all words from the RealWord table
#     return render(request, 'words/wordlist.html', {'words': words})


def wordlist_view(request):
    # Get all words from the database
    words = RealWord.objects.all()

    # Create a dictionary to organize words by their starting letter
    words_by_letter = {}
    for word in words:
        first_letter = word.word[0].upper()
        if first_letter not in words_by_letter:
            words_by_letter[first_letter] = []
        words_by_letter[first_letter].append(word)

    # List of letters for alphabet navigation
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    context = {
        'words_by_letter': words_by_letter,
        'alphabet': alphabet,
    }

    return render(request, 'words/wordlist.html', context)


def export_data_to_json(request):
    # Получаем все данные из модели RealWord
    words = RealWord.objects.all()
    
    # Сериализуем данные
    serializer = RealWordSerializer(words, many=True)
    data = serializer.data
    
    # Сохраняем JSON в файл
    file_path = os.path.join(settings.MEDIA_ROOT, 'exported_data.json')
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    
    return JsonResponse({'message': 'Data exported successfully!', 'file_path': file_path})


@csrf_exempt
def import_data_from_json(request):
    if request.method == 'POST':
        # Проверяем, был ли передан файл
        if 'file' not in request.FILES:
            return JsonResponse({'error': 'No file provided'}, status=400)

        json_file = request.FILES['file']

        # Читаем содержимое файла и парсим JSON
        try:
            data = json.load(json_file)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON file'}, status=400)

        # Обрабатываем каждый элемент в JSON-данных
        for word_data in data:
            # Создаем или получаем экземпляр RealWord
            word, created = RealWord.objects.get_or_create(
                word=word_data['word'],
                defaults={
                    'transcription': word_data.get('transcription', ''),
                    'definition': word_data.get('definition', ''),
                    'image': word_data.get('image', None)
                }
            )

            # Добавляем примеры, синонимы и антонимы
            if 'examples' in word_data:
                for example in word_data['examples']:
                    Example.objects.get_or_create(word=word, text=example['text'])

            if 'synonyms' in word_data:
                for synonym in word_data['synonyms']:
                    Synonym.objects.get_or_create(word=word, text=synonym['text'])

            if 'antonyms' in word_data:
                for antonym in word_data['antonyms']:
                    Antonym.objects.get_or_create(word=word, text=antonym['text'])

        return JsonResponse({'message': 'Data imported successfully!'})

    return JsonResponse({'error': 'Invalid request method'}, status=405)
