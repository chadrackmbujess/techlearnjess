from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('comptes/', include('accounts.urls')),
    path('cours/', include('courses.urls')),
    path('forum/', include('forum.urls')),
    path('chat/', include('chat.urls')),
    path('certificats/', include('certificates.urls')),
    path('notifications/', include('notifications.urls')),
    path('paiements/', include('payments.urls')),
    path('sessions-live/', include('live_sessions.urls')),
]

# Servir les fichiers médias en développement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
