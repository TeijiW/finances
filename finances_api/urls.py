from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path("admin/", admin.site.urls),
    # path("core/", include("apps.core.urls")),
    path("page/", include("apps.page.urls")),
    path("budget/", include("apps.budget.urls")),
    path("expense/", include("apps.expense.urls")),
    path("api-token-auth/", obtain_auth_token),
]
