from django.contrib import admin
from .models import RealWord, Example, Synonym, Antonym


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
    list_display = ('word',)
    search_fields = ('word',)
    inlines = [ExampleInline, SynonymInline, AntonymInline]
