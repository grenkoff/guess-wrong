import json

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
                        # Создаем или получаем основной объект RealWord
                        word, created = RealWord.objects.get_or_create(
                            word=word_data['word'].lower(),
                            defaults={
                                'transcription': word_data.get('transcription', ''),
                                'definition': word_data.get('definition', ''),
                                'image': word_data.get('image', None)
                            }
                        )

                        # Обработка примеров
                        for example in word_data.get('examples', []):
                            Example.objects.get_or_create(word=word, text=example)

                        # Обработка синонимов
                        for synonym in word_data.get('synonyms', []):
                            Synonym.objects.get_or_create(word=word, text=synonym)

                        # Обработка антонимов
                        for antonym in word_data.get('antonyms', []):
                            Antonym.objects.get_or_create(word=word, text=antonym)

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
