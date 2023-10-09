from django.db import models
from datetime import datetime, timedelta
from users.models import grade_choices
from django.conf import settings


def get_return_date():
    return datetime.today() + timedelta(weeks=2)


class BookManager(models.Manager):
    def create_book(self, title):
        book = self.create(title=title)
        book.save()

        return book


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100, blank=True)
    objects = BookManager()

    def __str__(self):
        if self.author:
            return f"Title: {self.title}\n Author: {self.author}"
        return f"Title: {self.title}"


# book = Book.objects.create_book("Pride and Prejudice")


class Student(models.Model):
    student_first_name = models.CharField(
        max_length=100,
        help_text="Student First Name",
    )
    student_last_name = models.CharField(
        max_length=100,
        help_text="Student Last Name",
    )

    grade = models.CharField(max_length=35, choices=grade_choices)

    @property
    def student_name(self):
        return f"{self.student_first_name}.{self.student_last_name}"

    def __str__(self) -> str:
        return self.student_name


class CheckoutBook(models.Model):
    book = models.ForeignKey(
        Book, related_name="checkoutbook", on_delete=models.CASCADE
    )

    class Meta:
        verbose_name_plural = "Add Book to Check-out"


class CheckinBook(models.Model):
    book = models.ForeignKey(Book, related_name="checkinbook", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Add Book to Check-in"


class CheckoutorIn(models.Model):
    teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="teacher", on_delete=models.CASCADE
    )
    student = models.OneToOneField(
        Student, related_name="student", on_delete=models.CASCADE
    )

    check_in = models.ForeignKey(
        CheckinBook, null=True, related_name="checkin", on_delete=models.CASCADE
    )
    check_out = models.ForeignKey(
        CheckoutBook, null=True, related_name="checkout", on_delete=models.CASCADE
    )
    due_date = models.DateTimeField(default=get_return_date())
    date_checked_out = models.DateTimeField(auto_now_add=True)
    date_checked_in = models.DateTimeField(null=True, blank=True, auto_now_add=False)

    all_checked_in = models.BooleanField(default=False)

    @property
    def get_student_books(self, request, student_name):
        books = self.checkoutbook_set.all().filter(request.user).filter(student_name)
        books_list = [book for book in books]
        return books_list

    class Meta:
        verbose_name_plural = "Check In or Out"
