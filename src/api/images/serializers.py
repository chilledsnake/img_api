from rest_framework import serializers

from src.api.images.models import UploadedImages
from src.core.images.image_processing import ImageProcessor


class ImageSerializer(serializers.ModelSerializer):
    height = serializers.IntegerField(min_value=1, required=False)
    width = serializers.IntegerField(min_value=1, required=False)
    image_file = serializers.ImageField(write_only=True)

    class Meta:
        model = UploadedImages
        fields = ("id", "title", "url", "height", "width", "image_file")
        read_only_fields = ("id",)

    def create(self, validated_data):

        ImageProcessor(
            image_file=validated_data["image_file"].file,
            width=validated_data.pop("width", None),
            height=validated_data.pop("height", None),
        ).image_resize()

        return super().create(validated_data)
