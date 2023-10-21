from django.contrib import admin
from .models import Book, Student, CheckoutorIn, AddBookToCheckInOrOut


admin.site.register(Book)
admin.site.register(Student)
admin.site.register(AddBookToCheckInOrOut)
admin.site.register(CheckoutorIn)
