import json

from django.http import JsonResponse
from django.contrib import admin, messages
from django.shortcuts import render, redirect
from django.urls import path
from .models import RealWord, Example, Synonym, Antonym
from .forms import JSONUploadForm


class ExampleInline(admin.TabularInline):
    model = Example
    extra = 0
    fields = ('text',)


class SynonymInline(admin.TabularInline):
    model = Synonym
    extra = 0
    fields = ('text',)


class AntonymInline(admin.TabularInline):
    model = Antonym
    extra = 0
    fields = ('text',)


@admin.register(RealWord)
class RealWordAdmin(admin.ModelAdmin):
    list_display = ('word','transcription', 'short_definition')
    search_fields = ('word',)
    inlines = [ExampleInline, SynonymInline, AntonymInline]
    change_list_template = "admin/realword_changelist.html"

    def short_definition(self, obj):
        # Разбиваем строку на слова и берем первые 6
        definition_words = obj.definition.split()[:10]
        # Собираем строку из первых 6 слов и добавляем многоточие
        short_def = ' '.join(definition_words)
        if len(obj.definition.split()) > 10:
            short_def += '...'
        return short_def

    short_definition.short_description = 'Definition'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('import-json/', self.import_json, name='import_json'),
            path('export-json/', self.export_json, name='export_json'),
        ]
        return custom_urls + urls

    def import_json(self, request):
        if request.method == 'POST':
            form = JSONUploadForm(request.POST, request.FILES)
            if form.is_valid():
                json_file = request.FILES['json_file']
                try:
                    data = json.load(json_file)
                    for word_data in data:
                        # Найдем или создадим объект RealWord
                        word, created = RealWord.objects.update_or_create(
                            word=word_data['word'].lower(),  # Находим по слову
                            defaults={
                                'transcription': word_data.get('transcription', ''),
                                'definition': word_data.get('definition', ''),
                                'image': word_data.get('image', None)
                            }
                        )

                        # Обработка примеров
                        for example in word_data.get('examples', []):
                            Example.objects.update_or_create(word=word, text=example)

                        # Обработка синонимов
                        for synonym in word_data.get('synonyms', []):
                            Synonym.objects.update_or_create(word=word, text=synonym)

                        # Обработка антонимов
                        for antonym in word_data.get('antonyms', []):
                            Antonym.objects.update_or_create(word=word, text=antonym)

                    messages.success(request, "Данные успешно импортированы из JSON файла!")
                    return redirect("..")
                except json.JSONDecodeError:
                    messages.error(request, "Неверный формат JSON файла!")
                except KeyError as e:
                    messages.error(request, f"Отсутствует ключ в JSON: {e}")
                except TypeError as e:
                    messages.error(request, f"Ошибка в структуре JSON: {e}")
        else:
            form = JSONUploadForm()

        return render(request, 'admin/import_json.html', {'form': form})

    def export_json(self, request):
        words = RealWord.objects.all()
        data = []
        for word in words:
            data.append({
                'word': word.word,
                'transcription': word.transcription,
                'definition': word.definition,
                'examples': [example.text for example in word.examples.all()],
                'synonyms': [synonym.text for synonym in word.synonyms.all()],
                'antonyms': [antonym.text for antonym in word.antonyms.all()],
            })
        response = JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 2})
        response['Content-Disposition'] = 'attachment; filename="realwords.json"'
        return response
