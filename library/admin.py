from django.contrib import admin
from .models import Book, Student, CheckoutorIn, CheckOutOrder, AddBook


admin.site.register(Book)
admin.site.register(Student)
# admin.site.register(AddBookToCheckInOrOut)
admin.site.register(CheckoutorIn)
admin.site.register(CheckOutOrder)
admin.site.register(AddBook)
