from django.contrib import admin
from .models import PuzzlePage, RealWord, WrongWord, Example, Synonym, Antonym


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


@admin.register(PuzzlePage)
class PuzzlePageAdmin(admin.ModelAdmin):
    list_display = ('name', 'title')
    list_editable = ['title']

    def has_add_permission(self, request):
        return not PuzzlePage.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(RealWord)
class RealWordAdmin(admin.ModelAdmin):
    list_display = ('word',)
    search_fields = ('word',)
    inlines = [ExampleInline, SynonymInline, AntonymInline]


@admin.register(WrongWord)
class WrongWordAdmin(admin.ModelAdmin):
    list_display = ('word',)
    search_fields = ('word',)
