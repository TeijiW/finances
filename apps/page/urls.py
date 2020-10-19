from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.page.views import *

router = DefaultRouter()
router.register("", PageViewSet)

urlpatterns = [path("", include(router.urls))]
