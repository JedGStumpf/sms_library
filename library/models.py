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

    # student_name = models.CharField(max_length=100, default="")

    grade = models.IntegerField(choices=grade_choices)

    @property
    def student_name(self):
        return f"{self.student_first_name}.{self.student_last_name}"

    def __str__(self) -> str:
        return self.student_name


class CheckoutorIn(models.Model):
    student = models.ForeignKey(
        Student,
        related_name="student_checkoutorin",
        on_delete=models.CASCADE,
        null=True,
    )
    due_date = models.DateField(default=get_return_date())
    date_checked_out = models.DateField(null=True, blank=True, auto_now_add=False)
    date_checked_in = models.DateField(null=True, blank=True, auto_now_add=False)

    all_checked_in = models.BooleanField(default=False)

    @property
    def get_student_books(self, request, student_name):
        pass

    class Meta:
        verbose_name_plural = "Check Out or In"


class BookManager(models.Manager):
    def create_book(self, title, author=None):
        book = self.create(title=title, author=author)
        book.save()

        return book


class Book(models.Model):
    student = models.ForeignKey(
        Student, related_name="student_book", on_delete=models.CASCADE, null=True
    )
    check_out_or_in = models.ManyToManyField(
        CheckoutorIn,
        related_name="check_out_or_in_book",
    )
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100, blank=True)
    objects = BookManager()

    def __str__(self):
        if self.author:
            return f"Title: {self.title}\n Author: {self.author}"
        return f"Title: {self.title}"


class CheckOutOrder(models.Model):
    teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="teacher_order",
        on_delete=models.SET_NULL,
        null=True,
    )
    student = models.ForeignKey(
        Student, related_name="student_order", on_delete=models.SET_NULL, null=True
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
        CheckOutOrder, on_delete=models.SET_NULL, null=True, related_name="order"
    )
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50, null=True)

    class Meta:
        verbose_name_plural = "Add Books"

    def __str__(self):
        if self.author:
            return f"Title: {self.title}\n Author: {self.author}"
        return f"Title: {self.title}"
