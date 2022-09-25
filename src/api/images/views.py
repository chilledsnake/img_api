from rest_framework import filters, mixins, viewsets
from rest_framework.parsers import MultiPartParser

from src.api.images.models import UploadedImages
from src.api.images.serializers import ImageSerializer


class ImageViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = ImageSerializer
    queryset = UploadedImages.objects.all()

    lookup_field = "id"

    parser_classes = (MultiPartParser,)

    filter_backends = [
        filters.SearchFilter,
    ]
    search_fields = [
        "title",
    ]
