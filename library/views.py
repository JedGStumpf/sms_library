from typing import Any
from django.db import models
from django.db.models.query import QuerySet

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth import get_user_model

from .forms import (
    AddBookFormSet,
    CheckOutOrderForm,
)
from .models import CheckOutOrder, AddBook


def home_page(request):
    context = {"title": "Library Home"}
    return render(request, "library/library_home.html", context)


class CheckOutOrderInline:
    form_class = CheckOutOrderForm
    model = CheckOutOrder
    template_name = "library/create_or_update_order.html"

    def form_valid(self, form):
        named_formsets = self.get_named_formsets()
        if not all((form_val.is_valid() for form_val in named_formsets.values())):
            return self.render_to_response(self.get_context_data(form=form))

        self.object = form.save()

        # for every formset, attempt to find a specific formset save function
        # otherwise, just save.
        for name, formset in named_formsets.items():
            formset_save_func = getattr(self, "formset_{0}_valid".format(name), None)
            if formset_save_func is not None:
                formset_save_func(formset)
            else:
                formset.teacher = self.object
                formset.save()
        return redirect("library:order_list")

    def formset_books_valid(self, formset):
        """
        Used for Custom formset saving.  Useful if you have multiple formsets
        """
        add_books = formset.save(commit=False)

        for obj in formset.deleted_objects:
            obj.delete()
        for add_book in add_books:
            add_book.order = self.object
            add_book.save()


class OrderCreate(LoginRequiredMixin, CheckOutOrderInline, CreateView):
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super(OrderCreate, self).get_context_data(**kwargs)
        context["named_formsets"] = self.get_named_formsets()
        return context

    def get_named_formsets(self):
        if self.request.method == "GET":
            return {
                "books": AddBookFormSet(
                    prefix="books",
                ),
            }
        else:
            return {
                "books": AddBookFormSet(
                    self.request.POST or None,
                    self.request.FILES or None,
                    prefix="books",
                ),
            }

    def get_form_kwargs(self) -> dict[str, Any]:
        kwargs = super(OrderCreate, self).get_form_kwargs()
        kwargs["request"] = self.request

        return kwargs


# student=self.get_queryset()


class OrderUpdate(LoginRequiredMixin, CheckOutOrderInline, UpdateView):
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super(OrderUpdate, self).get_context_data(**kwargs)
        context["named_formsets"] = self.get_named_formsets()
        return context

    def get_named_formsets(self):
        return {
            "books": AddBookFormSet(
                self.request.POST or None,
                self.request.FILES or None,
                instance=self.object,
                prefix="books",
            ),
        }

    def get_form_kwargs(self) -> dict[str, Any]:
        kwargs = super(OrderUpdate, self).get_form_kwargs()
        kwargs["request"] = self.request

        return kwargs


class OrderList(LoginRequiredMixin, ListView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        return context

    def get_queryset(self, *args, **kwargs) -> QuerySet[Any]:
        user_grade = self.request.user.grade
        if user_grade == 9:
            return CheckOutOrder.objects.exclude(order_returned=True).filter(
                student__grade__gte=6
            )

        elif user_grade == 10:
            return CheckOutOrder.objects.all().exclude(order_returned=True)

        return CheckOutOrder.objects.exclude(order_returned=True).filter(
            student__grade=user_grade
        )

    model = CheckOutOrder

    template_name = "library/order_list.html"
    context_object_name = "orders"


@login_required
def delete_books(request, pk):
    try:
        book = AddBook.objects.get(id=pk)
    except AddBook.DoesNotExist:
        messages.success(request, "Book Does not Exist")
        return redirect("library:update_student", pk=book.student.id)

    book.delete()
    messages.success(request, "Book has been deleted")
    return redirect("library/student_list.html", pk=book.student.id)
