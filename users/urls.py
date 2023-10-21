from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import signup, CustomSignInView

app_name = "users"

urlpatterns = [

    path(
        "sign_in/",
        CustomSignInView.as_view(template_name="users/sign_in.html"),
        name="sign_in",
    ),
    path(
        "sign_out/",
        auth_views.LogoutView.as_view(template_name="users/sign_out.html"),
        name="sign_out",
    ),
    path("signup", signup, name="signup"),
]