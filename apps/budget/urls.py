from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.budget.views import *

router = DefaultRouter()
router.register("", BudgetViewSet)

urlpatterns = [path("", include(router.urls))]
