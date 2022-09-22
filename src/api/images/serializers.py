from rest_framework import serializers

from src.api.images.models import UploadedImages
from src.core.images.image_processing import ImageProcessor


class ImageSerializer(serializers.ModelSerializer):
    height = serializers.IntegerField(min_value=1)
    width = serializers.IntegerField(min_value=1)
    image_file = serializers.ImageField(write_only=True)

    class Meta:
        model = UploadedImages
        fields = ("id", "title", "url", "height", "width", "image_file")
        read_only_fields = ("id",)

    def create(self, validated_data):
        ImageProcessor(
            image_file=validated_data["image_file"].file,
            width=validated_data["width"],
            height=validated_data["height"],
        ).image_resize()

        instance, created = UploadedImages.objects.update_or_create(
            image_file_name=validated_data["image_file"].name,
            defaults={
                "image_file_name": validated_data["image_file"].name,
                "image_file": validated_data["image_file"],
                "title": validated_data["title"],
            },
        )
        return instance
