from django.test import TestCase
from .models import AddBook, CheckOutOrder, Student
from django.contrib.auth import get_user_model
from users.models import CustomUser


class AddBookTests(TestCase):
    def test_add_book(self):
        student = Student.objects.create(
            student_first_name="Molly", student_last_name="Stumpf", grade=2
        )
        User = get_user_model()
        user = User.objects.create_user(
            email="jedgstumpf@gmail.com", password="foo", grade=1
        )
        order = CheckOutOrder.objects.create(
            teacher=User.objects.get(email="jedgstumpf@gmail.com"),
            student=Student.objects.get(pk=1),
        )
        book = AddBook.objects.create(
            title="test Title", author="", returned=False, order_id=1
        )
        self.assertEqual(book.title, "test Title")
        self.assertEqual(book.author, "")
        self.assertFalse(book.returned)


class StudentTest(TestCase):
    def test_student(self):
        student = Student.objects.create(
            student_first_name="Molly", student_last_name="Stumpf", grade=2
        )
        self.assertEqual(student.student_last_name, "Stumpf")
        self.assertEqual(student.student_first_name, "Molly")
        self.assertEqual(student.grade, 2)


class CheckOutOrderTest(TestCase):
    def test_check_out_order(self):
        User = get_user_model()
        user = User.objects.create_user(
            email="jedgstumpf@gmail.com", password="foo", grade=1
        )
        student = Student.objects.create(
            student_first_name="Molly", student_last_name="Stumpf", grade=2
        )
        order = CheckOutOrder.objects.create(
            teacher=User.objects.get(email="jedgstumpf@gmail.com"),
            student=student,
        )
        self.assertEqual(order.order_returned, False)
