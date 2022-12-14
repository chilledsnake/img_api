import shutil
import typing as t

import pytest
from django.conf import settings
from django.test import Client
from factory.base import FactoryMetaClass
from rest_framework.reverse import reverse

from src.api.images.tests.utils import create_temp_image

pytestmark = pytest.mark.django_db(reset_sequences=True)


class TestImagesListView:
    @pytest.fixture()
    def url(self) -> str:
        return reverse("images_api:image-list")

    def test_no_images_should_return_empty_list(self, client: Client, url: str) -> None:
        response = client.get(url)
        assert response.status_code == 200
        assert response.data["results"] == []

    def test_one_image_exist(
        self, client: Client, url: str, uploaded_images_factory: FactoryMetaClass
    ) -> None:
        uploaded_images_factory()
        response = client.get(url)
        assert response.status_code == 200
        assert len(response.data["results"]) == 1

    @pytest.mark.parametrize(
        "filtering_keyword, expected_records_number",
        (
            pytest.param("test", 3, id="all_records"),
            pytest.param("test_1", 3, id="three_records"),
            pytest.param("test_1_2", 2, id="two records"),
            pytest.param("test_1_2_3", 1, id="one_record"),
            pytest.param("test_1_2_3_4", 0, id="empty"),
        ),
    )
    def test_list_filtering_by_title(
        self,
        client: Client,
        url: str,
        uploaded_images_factory: FactoryMetaClass,
        filtering_keyword: str,
        expected_records_number: int,
    ) -> None:
        uploaded_images_factory(title="test_1")
        uploaded_images_factory(title="test_1_2")
        uploaded_images_factory(title="test_1_2_3")
        response = client.get(f"{url}?search={filtering_keyword}")
        assert len(response.data["results"]) == expected_records_number


class TestImagesDetailView:
    @pytest.mark.parametrize(
        "id, result",
        (
            pytest.param("1", 200),
            pytest.param("0", 404),
        ),
    )
    def test_get_image(
        self,
        client: Client,
        uploaded_images_factory: FactoryMetaClass,
        id: str,
        result: int,
    ) -> None:
        uploaded_images_factory()
        response = client.get(reverse("images_api:image-detail", kwargs={"id": id}))
        assert response.status_code == result


class TestImagesCreateView:
    @pytest.fixture()
    def url(self) -> str:
        return reverse("images_api:image-list")

    def test_create_image_without_arguments_should_fail(
        self, client: Client, url: str
    ) -> None:
        response = client.post(url)
        expected_response = {
            "image_file": ["No file was submitted."],
        }
        assert response.status_code == 400
        assert response.data == expected_response

    @pytest.mark.parametrize("image_format", ("JPEG", "png", "PNG", "tiff", "TIFF"))
    def test_create_image(self, client: Client, url: str, image_format: str) -> None:
        temp_image = create_temp_image(image_format=image_format)
        post_data = {
            "image_file": temp_image,
            "title": "test",
            "height": 100,
            "width": 100,
        }
        response = client.post(path=url, data=post_data)
        assert response.status_code == 201
        assert response.data["width"] == post_data["width"]
        assert response.data["height"] == post_data["height"]

    @pytest.mark.parametrize(
        "width, height, required_width, required_height, expected_width, expected_height, status_code",
        (
            pytest.param(100, 50, 200, 200, 100, 50, 201, id="ratio 2/1"),
            pytest.param(200, 150, 100, 200, 100, 75, 201, id="ratio 4/3"),
            pytest.param(100, 200, 50, 400, 50, 100, 201, id="ratio 1/2"),
            pytest.param(
                100, 200, None, None, 100, 200, 201, id="no required dimensions"
            ),
            pytest.param(100, 200, None, 100, None, None, 400, id="no required width"),
            pytest.param(100, 200, 100, None, None, None, 400, id="no required height"),
        ),
    )
    def test_image_resize_and_optimization(
        self,
        client: Client,
        url: str,
        width: int,
        height: int,
        required_width: t.Union[int, None],
        required_height: t.Union[int, None],
        expected_width: t.Union[int, None],
        expected_height: t.Union[int, None],
        status_code: int,
    ) -> None:
        temp_image = create_temp_image(
            image_format="jpeg", width=width, height=height, name="test"
        )
        post_data = {
            "image_file": temp_image,
            "title": "test_2",
        }
        if required_width:
            post_data["width"] = required_width
        if required_height:
            post_data["height"] = required_height

        response = client.post(path=url, data=post_data)
        assert response.status_code == status_code
        if status_code == 201:
            assert response.data["width"] == expected_width
            assert response.data["height"] == expected_height


def teardown_module():
    shutil.rmtree(settings.MEDIA_ROOT)
