from django import forms
from django.forms import ModelForm, inlineformset_factory
from .models import Student, CheckOutOrder, AddBook
from django.contrib.auth import get_user_model


# user_grade = self.request.user.grade
# if user_grade == 9:
#     return CheckOutOrder.objects.exclude(order_returned=True).filter(
#         student__grade__gte=6
#     )

# elif user_grade == 10:
#     return CheckOutOrder.objects.all().exclude(order_returned=True)

# return CheckOutOrder.objects.exclude(order_returned=True).filter(
#     student__grade=user_grade
# )


class CheckOutOrderForm(ModelForm):
    def __init__(self, *args, **kwargs):
        try:
            self.request = kwargs.pop("request")
            teacher_grade = self.request.user.grade
            super(CheckOutOrderForm, self).__init__(*args, **kwargs)
            # ADD LOGIC FOR MIDDLE SCHOOL AND ALL
            if teacher_grade == 9:
                self.fields["student"].queryset = Student.objects.filter(
                    student__grade_get=6
                ).order_by("grade")
            elif teacher_grade == 10:
                self.fields["student"].queryset = Student.objects.all().order_by(
                    "grade"
                )
            else:
                self.fields["student"].queryset = Student.objects.filter(
                    grade=teacher_grade
                )
            self.fields["teacher"].queryset = get_user_model().objects.filter(
                id=self.request.user.id
            )
        except KeyError:
            super(CheckOutOrderForm, self).__init__(*args, **kwargs)

            if self.instance:
                kwargs_student_first_name = str(kwargs["instance"])
                kwargs_student_first_name = kwargs_student_first_name.split(".")[0]
                self.fields["student"].queryset = (
                    Student.objects.filter(
                        student_first_name=kwargs_student_first_name
                    ),
                )
                self.fields["teacher"].queryset = get_user_model().objects.filter(
                    id=self.request.user.id
                )

        # user_grade = self.request.user.grade
        # if user_grade == 9:
        #     return CheckOutOrder.objects.exclude(order_returned=True).filter(
        #         student__grade__gte=6
        #     )

        # elif user_grade == 10:
        #     return CheckOutOrder.objects.all().exclude(order_returned=True)

        # return CheckOutOrder.objects.exclude(order_returned=True).filter(
        #     student__grade=user_grade
        # )

    class Meta:
        model = CheckOutOrder
        fields = "__all__"
        # exclude = ["teacher"]

        widgets = {
            "due_date": forms.DateInput(
                attrs={"required": True, "class": "form-control"}
            ),
            "checked_out_on": forms.DateInput(
                attrs={"required": True, "class": "form-control"}
            ),
            "student": forms.Select(attrs={"required": True, "class": "form-control"}),
            "teacher": forms.Select(
                attrs={
                    "required": True,
                    "class": "form-control",
                },
            ),
        }


class AddBookForm(ModelForm):
    class Meta:
        model = AddBook
        fields = "__all__"


AddBookFormSet = inlineformset_factory(
    CheckOutOrder,
    AddBook,
    form=AddBookForm,
    extra=9,
    can_delete=False,
    can_delete_extra=True,
    min_num=1,
    validate_min=True,
)


# class StudentForm(ModelForm):
#     class Meta:
#         model = Student
#         exclude = ["teacher", "student_last_name", "grade", "student_first_name"]


# class CheckOutOrInForm(ModelForm):
#     class Meta:
#         model = CheckoutorIn
#         fields = "__all__"
#         exclude = ["student", "all_checked_in"]


# class BookForm(ModelForm):
#     class Meta:
#         model = Book
#         fields = "__all__"
#         exclude = ["student", "check_out_or_in"]
#         widgets = {
#             "date_checked_out": forms.DateInput(attrs={"class": "form-control"}),
#             "date_checked_in": forms.DateInput(attrs={"class": "form-control"}),
#         }


# CheckOutOrInFormSet = inlineformset_factory(
#     Student,
#     CheckoutorIn,
#     form=CheckOutOrInForm,
#     extra=1,
#     max_num=1,
#     min_num=1,
#     can_delete=True,
#     can_delete_extra=True,
# )


# BookFormSet = inlineformset_factory(
#     Student, Book, form=BookForm, extra=10, can_delete=True, can_delete_extra=True
# )
