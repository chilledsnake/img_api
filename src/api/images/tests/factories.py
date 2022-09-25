import factory.fuzzy

from src.api.images.models import UploadedImages


class UploadedImagesFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UploadedImages

    title = factory.fuzzy.FuzzyText()
    image_file = factory.django.ImageField()
