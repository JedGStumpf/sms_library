from django.contrib import admin
from .models import Student, CheckOutOrder, AddBook


class StudentAdmin(admin.ModelAdmin):
    @admin.action(description="Graduate and Move Grades +1 for All Students")
    def move_students_to_next_grade_or_graduate(self, request, queryset):

        for student in queryset:
            if student.grade == 8:
                student.delete()
            else:
                student.grade = student.grade + 1
                student.save()
        # queryset.update(grade=grade + 1)

    list_display = ["student_first_name", "student_last_name", "grade"]
    ordering = ["grade"]
    actions = [move_students_to_next_grade_or_graduate]


class BookAdmin(admin.ModelAdmin):
    @admin.action(description="Check in All Books: Select All At Year End Only")
    def check_in_all_books(self, request, queryset):

        for book in queryset:
            if not book.returned:
                book.returned = True
                book.save()

    actions = [check_in_all_books]


admin.site.register(Student, StudentAdmin)
admin.site.register(CheckOutOrder)
admin.site.register(AddBook, BookAdmin)
