from django.conf import settings
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from src.api.images.models import UploadedImages
from src.core.images.image_processing import ImageProcessor


class ImageSerializer(serializers.ModelSerializer):
    height = serializers.IntegerField(min_value=1, required=False)
    width = serializers.IntegerField(min_value=1, required=False)
    image_file = serializers.ImageField(write_only=True)
    url = serializers.SerializerMethodField()

    class Meta:
        model = UploadedImages
        fields = ("id", "title", "url", "height", "width", "image_file")
        read_only_fields = ("id",)

    def get_url(self, obj):

        if settings.USE_AWS_S3:
            return obj.image_file.url

        request = self.context.get("request")
        return request.build_absolute_uri(obj.image_file.url)

    def validate(self, attrs):
        width_height_attrs = (attrs.get("width", None), attrs.get("height", None))

        if not all(width_height_attrs) and any(width_height_attrs):
            raise ValidationError("Width and height required or none of them.")

        return attrs

    def create(self, validated_data):

        ImageProcessor(
            image_file=validated_data["image_file"].file,
            width=validated_data.pop("width", None),
            height=validated_data.pop("height", None),
        ).image_resize()

        return super().create(validated_data)
