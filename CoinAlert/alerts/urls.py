from django.urls import path
from django.conf import settings
from .views import ValueAlertViewSet,TimeAlertViewSet
from rest_framework import routers

app_name = 'alerts'

router = routers.DefaultRouter(trailing_slash=False)
router.register('api/alerts/time', TimeAlertViewSet, basename='alerts')
router.register('api/alerts/value', ValueAlertViewSet, basename='alerts')
urlpatterns = router.urls