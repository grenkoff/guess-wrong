from django.contrib import admin
from .models import RealWord, WrongWord

@admin.register(RealWord)
class RealWordAdmin(admin.ModelAdmin):
    list_display = ('word',)
    search_fields = ('word',)

@admin.register(WrongWord)
class FakeWordAdmin(admin.ModelAdmin):
    list_display = ('word',)
    search_fields = ('word',)
