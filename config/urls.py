from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

from drf_spectacular.views import (
    SpectacularSwaggerView,
)

from .apis import router

urlpatterns = [
    path("", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path('admin', admin.site.urls, name="admin"),
    path('api', include((router.urls, "api"), "api"), name="api"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
