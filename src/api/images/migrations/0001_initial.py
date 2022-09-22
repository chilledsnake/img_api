# Generated by Django 4.0.4 on 2022-09-21 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UploadedImages",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        blank=True, max_length=64, verbose_name="image title"
                    ),
                ),
                (
                    "image_file",
                    models.ImageField(
                        upload_to="images", verbose_name="uploaded image"
                    ),
                ),
                (
                    "image_file_name",
                    models.CharField(
                        blank=False, max_length=1024, verbose_name="image original name"
                    ),
                ),
            ],
        ),
    ]
