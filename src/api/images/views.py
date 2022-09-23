from rest_framework import filters, mixins, viewsets
from rest_framework.parsers import FormParser
from rest_framework.decorators import parser_classes

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
    filter_backends = [
        filters.SearchFilter,
    ]
    search_fields = [
        "title",
    ]
