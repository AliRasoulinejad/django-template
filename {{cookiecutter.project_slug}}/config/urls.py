from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django_prometheus import exports
from drf_spectacular.views import (
    SpectacularSwaggerView,
    SpectacularAPIView,
)

urlpatterns = [
    path("", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("schema", SpectacularAPIView.as_view(), name="schema"),
    path('admin/', admin.site.urls, name="admin"),
    path('api/', include(("applications.api.urls", "apis"))),

{%- if cookiecutter.use_metrics == "y" %}
    path("metrics", exports.ExportToDjangoView, name="prometheus-django-metrics"),
{%- endif %}
]

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls"))
    ]
    urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
