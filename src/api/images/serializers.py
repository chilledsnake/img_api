from rest_framework import serializers

from src.api.images.models import Image


class ImageSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    image_file = serializers.ImageField(write_only=True)

    class Meta:
        model = Image
        fields = ("id", "title", "url", "height", "width", "image_file")
        read_only_fields = ("id",)

    def get_url(self, obj):
        return obj.image_file.url
