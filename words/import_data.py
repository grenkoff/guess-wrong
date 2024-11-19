import json

from words.models import RealWord, Example, Synonym, Antonym

# Загружаем данные из JSON файла
with open('/home/grenkoff/Desktop/realwords.json', 'r') as file:
    data = json.load(file)

# Получаем общее количество элементов
total = len(data)

# Инициализируем счетчик
counter = 0

for entry in data:
    real_word, created = RealWord.objects.get_or_create(
        word=entry['word'],
        defaults={
            'transcription': entry.get('transcription', ''),
            'definition': entry['definition']
        }
    )

    if created:
        if 'examples' in entry:
            for example_text in entry['examples']:
                Example.objects.create(word=real_word, text=example_text)

        if 'synonyms' in entry:
            for synonym_text in entry['synonyms']:
                Synonym.objects.create(word=real_word, text=synonym_text)

        if 'antonyms' in entry:
            for antonym_text in entry['antonyms']:
                Antonym.objects.create(word=real_word, text=antonym_text)

    # Увеличиваем счетчик
    counter += 1

    # Выводим прогресс
    print(f'Обработано {counter}/{total} слов. Прогресс: {counter/total*100:.2f}%')
