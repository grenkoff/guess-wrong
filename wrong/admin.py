from django.contrib import admin
from .models import WrongWord


@admin.register(WrongWord)
class WrongWordAdmin(admin.ModelAdmin):
    list_display = ('word',)
    search_fields = ('word',)
