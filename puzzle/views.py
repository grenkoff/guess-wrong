import random

from django.shortcuts import render
from django.http import HttpResponse
from django.utils.safestring import mark_safe

from .models import RealWord, WrongWord
from pages.models import PuzzlePage


def puzzle_view(request):
    puzzle_page = PuzzlePage.objects.first()
    # Функция для генерации нового вопроса
    def generate_new_question():
        real_words = list(RealWord.objects.order_by('?')[:2])
        wrong_word = WrongWord.objects.order_by('?').first()

        # Проверяем, что есть достаточно слов для создания вопроса
        if len(real_words) < 2 or not wrong_word:
            return None, None, "Недостаточно слов для создания викторины."

        # Создаем список вариантов и перемешиваем их
        options = real_words + [wrong_word]
        random.shuffle(options)

        # Обновляем сессию с новым вопросом
        request.session['options'] = [word.word for word in options]
        request.session['wrong_word'] = wrong_word.word
        return request.session['options'], wrong_word.word, ""

    # Генерируем вопрос, если в сессии его нет
    if 'options' not in request.session or 'wrong_word' not in request.session:
        options, wrong_word, error_message = generate_new_question()
        if error_message:
            return HttpResponse(error_message)
    else:
        options = request.session['options']
        wrong_word = request.session['wrong_word']

    # Обработка ответа пользователя
    if request.method == "POST":
        selected_word = request.POST.get('selected_word')
        wrong_word = request.session['wrong_word']

        if selected_word == wrong_word:
            message = mark_safe(f"Ура! Ты угадал неправильное слово <strong>{selected_word}</strong>")
        else:
            message = mark_safe(f"На самом деле слово <strong>{selected_word}</strong> существует")

        # Очищаем текущий вопрос из сессии и генерируем новый
        del request.session['options']
        del request.session['wrong_word']
        
        # Генерируем новый вопрос
        options, wrong_word, error_message = generate_new_question()
        if error_message:
            return HttpResponse(error_message)

        return render(request, 'pages/puzzle.html', {
            'options': options,
            'message': message,
            'puzzle_page': puzzle_page
        })

    # При GET-запросе отображаем начальный вопрос
    return render(request, 'pages/puzzle.html', {'options': options, 'puzzle_page': puzzle_page})
