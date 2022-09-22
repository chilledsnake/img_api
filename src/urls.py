from django.urls import include, path

from src.api.images import urls as image_urls
from swagger.conf import schema_view

urlpatterns = [
    path("", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("images/", include(image_urls)),
]
