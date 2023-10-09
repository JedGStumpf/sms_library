from django.contrib import admin
from .models import Book, Student, CheckoutBook, CheckoutorIn, CheckinBook


admin.site.register(Book)
admin.site.register(Student)
admin.site.register(CheckinBook)
admin.site.register(CheckoutBook)
admin.site.register(CheckoutorIn)
