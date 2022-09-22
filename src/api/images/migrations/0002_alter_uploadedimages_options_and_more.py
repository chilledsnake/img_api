# Generated by Django 4.0.4 on 2022-09-22 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("images", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="uploadedimages",
            options={"ordering": ["id"]},
        ),
        migrations.AlterField(
            model_name="uploadedimages",
            name="image_file",
            field=models.ImageField(
                upload_to="images", verbose_name="uploaded image"
            ),
        ),
    ]