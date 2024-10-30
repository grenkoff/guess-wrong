import random
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.safestring import mark_safe
from .models import PuzzlePage, RealWord, WrongWord

def puzzle_view(request):
    puzzle_page = PuzzlePage.objects.first()

    # Функция для генерации нового вопроса
    def generate_new_question():
        real_words = list(RealWord.objects.order_by('?')[:2])
        wrong_word = WrongWord.objects.order_by('?').first()

        options = real_words + [wrong_word]
        random.shuffle(options)

        # Сохраняем новый вопрос в сессии
        request.session['options'] = [word.word for word in options]
        request.session['wrong_word'] = wrong_word.word
        request.session['incorrect_attempts'] = []  # Сбрасываем предыдущие попытки
        request.session['message'] = mark_safe("Hello!<br>Guess the <u>wrong</u> word.")  # Начальное сообщение

        return request.session['options'], wrong_word.word, ""

    # Генерируем вопрос, если его нет в сессии
    if 'options' not in request.session or 'wrong_word' not in request.session:
        options, wrong_word, error_message = generate_new_question()
        if error_message:
            return HttpResponse(error_message)
        message = request.session.get('message', "")
    else:
        options = request.session['options']
        wrong_word = request.session['wrong_word']
        message = request.session.get('message', "")

    # Обработка ответа
    if request.method == "POST":
        selected_word = request.POST.get('selected_word')

        if selected_word == wrong_word:
            message = mark_safe("<span class='success-message'>You got it!</span><br>Guess the <u>wrong</u> word now.")
            del request.session['options']
            del request.session['wrong_word']
            options, wrong_word, error_message = generate_new_question()
            if error_message:
                return HttpResponse(error_message)
        else:
            message = mark_safe(f"<span class='fail-message'>The word</span> <strong>'{selected_word}'</strong> <span class='fail-message'>exists.</span><br>Try to guess the <u>wrong</u> word again.")
            if 'incorrect_attempts' not in request.session:
                request.session['incorrect_attempts'] = []
            request.session['incorrect_attempts'].append(selected_word)
            request.session.modified = True  # Обновляем сессию

        request.session['message'] = message  # Сохраняем текущее сообщение в сессии

        return render(request, 'puzzle/puzzle.html', {
            'options': options,
            'message': message,
            'puzzle_page': puzzle_page,
            'incorrect_attempts': request.session.get('incorrect_attempts', []),
            'is_correct': selected_word == wrong_word
        })

    # Начальный GET-запрос
    return render(request, 'puzzle/puzzle.html', {
        'options': options,
        'puzzle_page': puzzle_page,
        'message': message,
        'incorrect_attempts': request.session.get('incorrect_attempts', [])
    })
