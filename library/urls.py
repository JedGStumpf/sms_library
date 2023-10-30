from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

from library.views import (
    OrderList,
    OrderUpdate,
    OrderCreate,
    delete_books,
)


app_name = "library"

urlpatterns = [
    path("", views.home_page, name="home"),
    path("order_list/", OrderList.as_view(), name="order_list"),
    path("create_order/", OrderCreate.as_view(), name="create_order"),
    path("update_order/<int:pk>/", OrderUpdate.as_view(), name="update_order"),
    path("delete-books/<int:pk>/", delete_books, name="delete_books"),
]
