from django.db import models
from datetime import date, timedelta
from users.models import grade_choices
from django.conf import settings
from django.utils import timezone
from users.models import CustomUser


# Students can only have grades 0-8 (K-8)
student_grade_choices = grade_choices[0:9]

DEFAULT_TEACHER = CustomUser.objects.get(email="library@stmesc.org").id


def get_return_date():
    today = date.today()
    return today + timedelta(weeks=2)


class Student(models.Model):
    """
        Model defining fields to create a
        new student
    """
    student_first_name = models.CharField(
        max_length=100,
        help_text="Student First Name",
    )
    student_last_name = models.CharField(
        max_length=100,
        help_text="Student Last Name",
    )

    grade = models.IntegerField(choices=student_grade_choices, blank=False)

    @property
    def student_name(self):
        return f"{self.student_first_name}.{self.student_last_name}"

    def __str__(self) -> str:
        return self.student_name


class CheckOutOrder(models.Model):
    """
        Model to create a new order, foreignkeys
        to both a user instance and a student instance
        tying this order to both instances on creation
    """
    teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="teacher_order",
        on_delete=models.SET_DEFAULT,
        default=DEFAULT_TEACHER,
    )
    student = models.ForeignKey(
        Student, related_name="student_order", on_delete=models.CASCADE
    )
    checked_out_on = models.DateField(default=timezone.now, blank=True, null=True)
    due_date = models.DateField(default=get_return_date(), blank=True, null=True)
    order_returned = models.BooleanField(
        verbose_name="Return All Books And Close Order", default=False
    )

    def __str__(self):
        return f"{self.student.student_name} \nChecked Out On: {self.checked_out_on}"

    class Meta:
        verbose_name_plural = "Check Out Orders"


class AddBook(models.Model):
    """
        Model to create a new book instance
        Foreignkey to CheckOutOrder tying a created book
        to an order
    """
    order = models.ForeignKey(
        CheckOutOrder, on_delete=models.CASCADE, related_name="order"
    )
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50, null=True)
    returned = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Books"

    def __str__(self):
        if self.author:
            return f"Title: {self.title}\n Author: {self.author}"
        return f"Title: {self.title}"
