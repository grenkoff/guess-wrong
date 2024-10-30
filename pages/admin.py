from django.contrib import admin

from .models import HomePage

@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    list_display = ('name', 'domain', 'title')
    list_editable = ['domain', 'title']

    def has_add_permission(self, request):
        return not HomePage.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False
