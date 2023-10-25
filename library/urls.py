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
    # path("student_list/", StudentList.as_view(), name="student_list"),
    # path("create_student/", StudentCreate.as_view(), name="create_student"),
    # path(
    #     "update_student/<int:pk>/",
    #     StudentUpdate.as_view(),
    #     name="update_student",
    # ),
    # path("delete-book/<int:pk>/", delete_book, name="delete_book"),
    # path(
    #     "delete-order/<int:pk>/", delete_check_out_or_in, name="delete_check_out_or_in"
    # ),
    # path("checkoutorin/", CheckOutOrInView.as_view(), name="checkoutorin"),
    # path("checkout/", CheckOutView.as_view(), name="checkout"),
]
