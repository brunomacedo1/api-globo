from django.conf.urls import url, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('cards', CardSpecsViewSet)

urlpatterns = [
  url('', include(router.urls))
]