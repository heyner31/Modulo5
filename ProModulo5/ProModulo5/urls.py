from django.contrib import admin
from django.urls import path, include, re_path
from core import views
from core.urls import core_urlpatterns
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(core_urlpatterns)),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)