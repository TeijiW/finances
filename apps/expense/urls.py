from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.expense.views import *

router = DefaultRouter()
router.register("", ExpenseViewSet)

urlpatterns = [path("", include(router.urls))]
