from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path("admin/", admin.site.urls),
    path("site/", include("apps.site.urls")),
    path("api/page/", include("apps.page.urls")),
    path("api/budget/", include("apps.budget.urls")),
    path("api/expense/", include("apps.expense.urls")),
    path("api/api-token-auth/", obtain_auth_token),
]
