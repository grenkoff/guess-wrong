from django.contrib import admin
from .models import PuzzlePage, RealWord, WrongWord


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


@admin.register(WrongWord)
class FakeWordAdmin(admin.ModelAdmin):
    list_display = ('word',)
    search_fields = ('word',)
