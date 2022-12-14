from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="Image API",
        default_version="v1",
        description="Api documentation",
        contact=openapi.Contact(email="cwroblewski@o2.pl"),
    ),
    public=True,
)
