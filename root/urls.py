from unicodedata import name
from django.contrib import admin
from django.urls import path
from root import settings
from django.conf.urls.static import static

from apps.views import homeview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeview, name='home'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)