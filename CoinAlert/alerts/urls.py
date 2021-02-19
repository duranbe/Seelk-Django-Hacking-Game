from django.urls import path
from django.conf import settings
from .views import AlertViewSet
from rest_framework import routers

app_name = 'alerts'

router = routers.DefaultRouter(trailing_slash=False)
router.register('api/alerts', AlertViewSet, basename='alerts')
urlpatterns = router.urls