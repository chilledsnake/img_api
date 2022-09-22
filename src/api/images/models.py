from django.db import models


class Image(models.Model):
    title = models.CharField(verbose_name="image title", max_length=64, blank=True)
    height = models.PositiveIntegerField(verbose_name="required image height")
    width = models.PositiveIntegerField(verbose_name="required image width")
    image_file = models.ImageField(verbose_name="uploaded image", upload_to="images")

    class Meta:
        ordering = [
            "id",
        ]
