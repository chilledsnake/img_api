import os
import typing as t

from django.conf import settings
from PIL import Image


def create_temp_image(
    width: t.Union[int, None] = 100,
    height: t.Union[int, None] = 100,
    color: t.Tuple[int, int, int] = (256, 0, 0),
    image_format: str = "JPEG",
    image_palette: str = "RGB",
    name: str = "test",
) -> str:
    if not os.path.exists(settings.MEDIA_ROOT):
        os.mkdir(settings.MEDIA_ROOT)
    file_name = f"{settings.MEDIA_ROOT}/{name}.{image_format}"
    with Image.new(image_palette, (width, height), color) as thumb:
        thumb.save(file_name, format=image_format, width=width, height=height)
    return file_name
