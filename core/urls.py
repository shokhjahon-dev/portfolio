from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from core import settings
from contact.views import IndexView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView, name="index"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)