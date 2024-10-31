from django.contrib import admin
from .models import SigninPage


@admin.register(SigninPage)
class PuzzlePageAdmin(admin.ModelAdmin):
    list_display = ('name', 'title')
    list_editable = ['title']

    def has_add_permission(self, request):
        return not SigninPage.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False
