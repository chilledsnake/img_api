from io import BytesIO

from django.core.files import File
from PIL import Image


def create_temp_image(
    width=100,
    height=100,
    color=(256, 0, 0),
    image_format="JPEG",
    image_palette="RGB",
    name="test",
):
    file_name = name + "." + image_format
    file = BytesIO()
    with Image.new(image_palette, (width, height), color) as thumb:
        thumb.save(file, format=image_format, width=width, height=height)
        file.seek(0)
    return File(file, name=file_name)
