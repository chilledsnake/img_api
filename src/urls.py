from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from src.api.images import urls as image_urls
from swagger.conf import schema_view

urlpatterns = [
    path("", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("images/", include(image_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
