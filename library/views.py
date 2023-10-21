from typing import Any
import functools
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.conf import settings
from django.utils.decorators import method_decorator

from .models import Student


# def needs_new_password(view_func):
#     @functools.wraps(view_func)
#     def wrapper(request, *args, **kwargs):
#         if request.user.needs_reset_email:
#             if request.user.is_superuser is False:
#                 return redirect("password_reset")

#     return wrapper


def home_page(request):
    # user = request.user
    # if user.is_authenticated:
    #     if user.needs_reset_email:
    #         if user.is_superuser is False:
    #             return redirect("password_reset")
    context = {"title": "Library Home"}
    return render(request, "library/library_home.html", context)


@method_decorator(login_required, name="dispatch")
class StudentListView(ListView):
    model = Student
    context_object_name = "students"

    def get_queryset(self, *args, **kwargs):
        qs = super(StudentListView, self).get_queryset(*args, **kwargs)
        qs = qs.order_by("grade")
        return qs

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context