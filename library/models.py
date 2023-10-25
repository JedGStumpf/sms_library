from django.db import models
from datetime import date, timedelta
from users.models import grade_choices
from django.conf import settings
from django.utils import timezone


def get_return_date():
    today = date.today()
    return today + timedelta(weeks=2)


class Student(models.Model):
    teacher = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="student",
    )
    student_first_name = models.CharField(
        max_length=100,
        help_text="Student First Name",
    )
    student_last_name = models.CharField(
        max_length=100,
        help_text="Student Last Name",
    )

    grade = models.IntegerField(choices=grade_choices)

    @property
    def student_name(self):
        return f"{self.student_first_name}.{self.student_last_name}"

    def __str__(self) -> str:
        return self.student_name


class CheckOutOrder(models.Model):
    teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="teacher_order",
        on_delete=models.SET_DEFAULT,
        default=1,
    )
    student = models.ForeignKey(
        Student, related_name="student_order", on_delete=models.CASCADE
    )
    due_date = models.DateField(default=get_return_date())
    checked_out_on = models.DateField(default=timezone.now)
    order_returned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.student_name} \nChecked Out On: {self.checked_out_on}"

    class Meta:
        verbose_name_plural = "Check Out Orders"


class AddBook(models.Model):
    order = models.ForeignKey(
        CheckOutOrder, on_delete=models.CASCADE, related_name="order"
    )
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50, null=True)

    class Meta:
        verbose_name_plural = "Add Books"

    def __str__(self):
        if self.author:
            return f"Title: {self.title}\n Author: {self.author}"
        return f"Title: {self.title}"
