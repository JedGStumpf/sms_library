from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.home_page, name="home"),
    path(
        "sign_in/",
        auth_views.LoginView.as_view(template_name="library/sign_in.html"),
        name="sign_in",
    ),
    path(
        "sign_out/",
        auth_views.LogoutView.as_view(template_name="library/sign_out.html"),
        name="sign_out",
    ),
]
