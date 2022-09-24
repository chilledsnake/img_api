import os

from django.conf import settings
from pytest_factoryboy import register

from src.api.images.tests.factories import UploadedImagesFactory


def pytest_configure():
    settings.USE_AWS_S3 = False
    settings.MEDIA_URL = "/media/"
    settings.MEDIA_ROOT = os.path.join(settings.BASE_DIR, "media")


register(UploadedImagesFactory)
