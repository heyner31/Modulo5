from django.contrib import admin
from django.urls import path, include, re_path
from core import views
from core.urls import core_urlpatterns
from services.urls import Services_urlpatterns
from contact.urls import contact_urlpatterns
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(core_urlpatterns)),
    path('services/', include(Services_urlpatterns)),
    path('contact/', include(contact_urlpatterns)),
    # Ckeditor path
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)

admin.site.site_header = "IA-WEB"
admin.site.index_title = "Panel de administrador IA-WEB"
admin.site.title = "3"