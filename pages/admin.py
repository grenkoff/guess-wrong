from django.contrib import admin

from .models import HomePage, PuzzlePage

@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    list_display = ('name', 'domain', 'title')
    list_editable = ['domain', 'title']

    def has_add_permission(self, request):
        return not HomePage.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)


@admin.register(PuzzlePage)
class HomePageAdmin(admin.ModelAdmin):
    list_display = ('name', 'title')
    list_editable = ['title']

    def has_add_permission(self, request):
        return not PuzzlePage.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
