from django.db import models


class UploadedImages(models.Model):
    title = models.CharField(verbose_name="image title", max_length=64, blank=True)
    image_file = models.ImageField(verbose_name="uploaded image", upload_to="images")

    class Meta:
        ordering = [
            "id",
        ]

    @property
    def height(self):
        return self.image_file.height

    @property
    def width(self):
        return self.image_file.width
