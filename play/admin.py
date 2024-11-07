from django.contrib import admin
from .models import PlayPage


@admin.register(PlayPage)
class PlayPageAdmin(admin.ModelAdmin):
    list_display = ('name', 'title')
    list_editable = ['title']

    def has_add_permission(self, request):
        return not PlayPage.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False
