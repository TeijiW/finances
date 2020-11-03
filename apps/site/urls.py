from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views

from apps.site.views import Home
from apps.site.forms import UserLoginForm

urlpatterns = [
    url("home/", Home.as_view(), name="home"),
    path(
        "accounts/login/",
        views.LoginView.as_view(
            authentication_form=UserLoginForm,
            template_name="login.html",
            redirect_authenticated_user=True,
        ),
        name="login",
    ),
]
