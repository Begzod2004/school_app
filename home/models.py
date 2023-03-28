from django.db import models
from django.contrib.auth.models import AbstractUser
from parler.models import TranslatableModel, TranslatedFields
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import BaseUserManager
from account.models import *
from datetime import date

# class UserManager(BaseUserManager):
#     """Manager for users."""

#     def create_user(self, email, password=None, **extra_fields):
#         """Create, save and return a new user."""
#         if not email:
#             raise ValueError('User must have an email address.')
#         user = self.model(email=self.normalize_email(email), **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)

#         return user

#     def create_superuser(self, email, password, **extra_fields):
#         """Create and return a new superuser."""
#         extra_fields.setdefault('is_staff', True)   
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')

#         return self.create_user(email, password, **extra_fields)

# class User(AbstractUser):
#     USER_TYPE_CHOICES = (
#         ('admin', 'Admin'),
#         ('teacher', 'Teacher'),
#         ('student', 'Student'),
#         ('parent', 'Parent'),
#         ('registrar', 'Registrar'),
#     )

#     user_type = models.CharField(choices=USER_TYPE_CHOICES, max_length=20)
#     full_name = models.CharField(max_length=255)
#     username = models.CharField(max_length=255, unique=True)
#     date_of_birth = models.DateField(null=True, blank=True)
#     gender = models.CharField(max_length=10, null=True, blank=True)
#     objects = UserManager()
#     USERNAME_FIELD = 'username'

#     def __str__(self):
#         return self.full_name
    
#     class Meta:
#         verbose_name = "Foydalanuvchi"
#         verbose_name_plural = "Foydalanuvchilar"

    

class Course(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=100, verbose_name=_('Nomi')),
        description = models.TextField(verbose_name=_('Qisqacha malumot'))
    )
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name=_('Narxi'))

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Kurs"
        verbose_name_plural = "Kurslar"


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
    groups = models.ManyToManyField('Group')
    phone_number = PhoneNumberField(blank=True, null=True, verbose_name=_("Telefon raqami"), help_text=_("O'zbekiston telefon raqamini kiriting"))

    def __str__(self):
        return self.user.full_name


class Registrar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.full_name


class Class(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
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

