from django.contrib import admin
from .models import Student, CheckOutOrder, AddBook


admin.site.register(Student)
admin.site.register(CheckOutOrder)
admin.site.register(AddBook)
