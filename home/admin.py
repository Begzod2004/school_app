from django.contrib import admin
from .models import *
from parler.admin import TranslatableAdmin
# Register your models here.
class CourseAdmin(TranslatableAdmin):
    list_display = ['name', 'description']




admin.site.register(Course, CourseAdmin)
admin.site.register(User)
admin.site.register(Teacher)
admin.site.register(Parent)
admin.site.register(Student)
admin.site.register(Registrar)
admin.site.register(Class)
admin.site.register(Lesson)
admin.site.register(Attendance)
admin.site.register(Group)
admin.site.register(Invoice)
admin.site.register(Payment)
admin.site.register(Announcement)