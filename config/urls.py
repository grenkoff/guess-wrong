"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from pages.views import page_not_found
from words.views import import_data_from_json #export_data_to_json,

urlpatterns = [
    path('admin/', admin.site.urls),
    path('words/', include('words.urls', namespace='words')),
    path('play/', include('play.urls', namespace='play')),
    # path('export-json/', export_data_to_json, name='export_json'),
    path('import-json/', import_data_from_json, name='import_json'),
    path('', include('pages.urls', namespace='pages')),
    path('', include('sim.urls', namespace='sim')),
    path("django-check-seo/", include("django_check_seo.urls")),
]

handler404 = page_not_found

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
