from django.urls import path
from django.conf import settings
from .views import ValueAlertViewSet, TimeAlertViewSet
from rest_framework import routers

app_name = "alerts"

router = routers.DefaultRouter(trailing_slash=False)
router.register(
    "api/alerts/time", TimeAlertViewSet, basename="alerts"
)  # Time Alert CRUD
router.register(
    "api/alerts/value", ValueAlertViewSet, basename="alerts"
)  # Value Alert CRUD
urlpatterns = router.urls
