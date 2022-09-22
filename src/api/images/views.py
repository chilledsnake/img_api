from rest_framework import filters, mixins, viewsets

from src.api.images.models import Image
from src.api.images.serializers import ImageSerializer


class ImageViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):

    serializer_class = ImageSerializer
    queryset = Image.objects.all()
    lookup_field = "id"
    filter_backends = [
        filters.SearchFilter,
    ]
    search_fields = [
        "title",
    ]
