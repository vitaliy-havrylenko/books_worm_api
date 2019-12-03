from django.contrib import admin
from django.conf import settings
from django.urls import path, include


api_urlpatterns = [
    path('', include('apps.accounts.urls'), name='accounts'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(api_urlpatterns), name='api'),
]

# enable serve static by django for local development
if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )