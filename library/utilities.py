from django.contrib.auth import get_user_model
from .models import Book, BookManager, CheckoutorIn, AddBookToCheckInOrOut
from library.models import Student


def checkout_data(request):
    if request.user.is_authenticated():
        teacher = get_user_model()
        students = Student.objects.all()


def get_current_user(request):
    return request.user
