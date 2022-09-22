from rest_framework.routers import DefaultRouter

from src.api.images.views import ImageViewSet

app_name = "shortener"

router = DefaultRouter()
router.register(r"", ImageViewSet, basename="image")
urlpatterns = router.urls
