from django.db import models
from django.contrib.auth.models import AbstractUser
from parler.models import TranslatableModel, TranslatedFields
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import BaseUserManager
from account.models import *
from datetime import date


class Course(models.Model): # Fan qaysiligi
    name = models.CharField(max_length=100)
    description = models.TextField()


    def __str__(self):
        return self.name

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course)
    salary = models.DecimalField(max_digits=6, decimal_places=2)
    lessons_per_month = models.IntegerField()

    def __str__(self):
        return self.user.full_name


class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    children = models.ManyToManyField('Student')

    def __str__(self):
        return self.user.full_name
 

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course)
    teachers = models.ManyToManyField(Teacher)
    attendance = models.ManyToManyField('Lesson')
    phone_number = PhoneNumberField(blank=True, null=True, verbose_name=_("Telefon raqami"), help_text=_("O'zbekiston telefon raqamini kiriting"))

    def __str__(self):
        return self.user.full_name


class Registrar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.full_name


class Class(models.Model): # Dars otadigan Sinif 
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE) # Darsda otiladigan fanlar
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.course} class by {self.teacher} for {self.student}"


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    homework = models.FileField(upload_to='media/homework')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.course} - {self.date}"


class Attendance(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendances')
    is_present = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student} - {self.lesson.course} - {self.lesson.date}"

class Group(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.name
    
class Invoice(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    issue_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    is_paid = models.BooleanField(default=False)

    @property
    def is_past_due(self):
        return date.today() > self.due_date and not self.is_paid

    def save(self, *args, **kwargs):
        if self.is_past_due:
            self.is_paid = False
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student} - {self.course} - {self.amount}"


class Payment(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.invoice.student} - {self.date}"


class Announcement(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

DAYS_OF_WEEK = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday'),
)

class LessonSchedule(models.Model): # Dars jadvali
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)
    day_of_week = models.CharField(choices=DAYS_OF_WEEK, max_length=20)
    start_time = models.TimeField()
    end_time = models.TimeField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.class_name} - {self.day_of_week} - {self.start_time} to {self.end_time}"


