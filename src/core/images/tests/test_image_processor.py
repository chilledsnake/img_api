import shutil
import typing as t

import pytest
from django.conf import settings
from django.core.files import File
from PIL import Image

from src.core.images.image_processing import ImageProcessor
from src.core.images.tests.utils import create_temp_image

pytestmark = pytest.mark.django_db(reset_sequences=True)


class TestImageProcessor:
    @pytest.mark.parametrize(
        "width, height, required_width, required_height, expected_width, expected_height",
        (
            pytest.param(100, 50, 200, 200, 100, 50, id="ratio 2/1"),
            pytest.param(200, 150, 100, 200, 100, 75, id="ratio 4/3"),
            pytest.param(100, 200, 50, 400, 50, 100, id="ratio 1/2"),
            pytest.param(100, 200, None, None, 100, 200, id="no required dimensions"),
            pytest.param(100, 200, None, 100, 100, 200, id="no required width"),
            pytest.param(100, 200, 100, None, 100, 200, id="no required height"),
        ),
    )
    def test_resize(
        self,
        width: int,
        height: int,
        required_width: t.Union[int, None],
        required_height: t.Union[int, None],
        expected_width: int,
        expected_height: int,
    ) -> None:
        image = create_temp_image(width=width, height=height)
        ImageProcessor(
            image_file=File(open(image, "rb"), name=image),
            width=required_width,
            height=required_height,
        ).image_resize()

        with Image.open(image) as _image:
            assert _image.width == expected_width
            assert _image.height == expected_height


def teardown_module():
    shutil.rmtree(settings.MEDIA_ROOT)
