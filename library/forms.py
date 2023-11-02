from django import forms
from django.forms import ModelForm, inlineformset_factory
from .models import Student, CheckOutOrder, AddBook
from django.contrib.auth import get_user_model


class CheckOutOrderForm(ModelForm):
    """
        Very Custom Form to Create or Update an Order
        Derived from this tutorial:
        letscodemore.com/blog/django-inline-formset-factory-with-examples/
        
        Checks if it is an update form and omits the
        order_returned field if it is not
        
        Has custom query logic to tie the current users
        grade to only view students of the same grade
    """

    def __init__(self, *args, **kwargs):
        try:
            self.request = kwargs.pop("request")
            teacher_grade = self.request.user.grade
            super(CheckOutOrderForm, self).__init__(*args, **kwargs)
            # ADD LOGIC FOR MIDDLE SCHOOL AND ALL
            if "update" not in str(self.request):

                self.fields["order_returned"].widget = forms.HiddenInput()
                self.fields["order_returned"].label = ""
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

    class Meta:
        model = CheckOutOrder
        fields = "__all__"
        widgets = {
            "due_date": forms.SelectDateWidget(
                attrs={
                    "class": "form-control",
                    "readonly": True,
                    "disabled": True,
                }
            ),
            "checked_out_on": forms.SelectDateWidget(
                attrs={
                    "class": "form-control",
                    "readonly": True,
                    "disabled": True,
                }
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
