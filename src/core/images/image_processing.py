import typing as t

from django.core.files import File
from PIL import Image


class ImageProcessor:
    def __init__(
        self,
        image_file: File,
        width: t.Union[int, None] = None,
        height: t.Union[int, None] = None,
    ):
        self.image_file = image_file
        self.width = width
        self.height = height

    def image_resize(self) -> None:
        if all((self.width, self.height)):
            with Image.open(self.image_file) as image:
                image.thumbnail((self.width, self.height))
                image.save(self.image_file.name, format=image.format)
