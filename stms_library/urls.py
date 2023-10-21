from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from library import views
from users import views
from users.views import ResetPasswordView, CustomSignInView
from users.forms import SignInForm, CustomPasswordResetForm
from django.contrib.admin.sites import AdminSite

admin.site.site_title = "St. Mary School Library Admin"
admin.site.site_header = "St. Mary School Library Admin"
admin.site.index_title = "St. Mary School Library Admin Menu"


AdminSite.login_form = SignInForm
AdminSite.login_template = "users/login.html"


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("library.urls")),
    path("", include("users.urls")),
    path(
        "users:password-reset/",
        ResetPasswordView.as_view(form_class=CustomPasswordResetForm),
        name="password_reset",
    ),
    path(
        "users:password-reset-confirm/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="users/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "users:password-reset-complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="users/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    path("captcha/", include("captcha.urls")),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
