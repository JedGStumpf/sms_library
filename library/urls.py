from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from library.views import StudentListView

app_name = "library"

urlpatterns = [
    path("", views.home_page, name="home"),
    path("student_list/", StudentListView.as_view(), name="student_list"),
]
