from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from rest_framework import routers
from rest_framework.response import Response

app_name = 'users'

from .views import AuthViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register('api/auth', AuthViewSet, basename='auth')
urlpatterns = router.urls