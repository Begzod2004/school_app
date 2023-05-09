from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.response import Response
from account.api.v1.serializers import RegisterSerializer
from .models import (
    Course,
    Teacher,
    Parent,
    Student,
    Registrar,
)
from .serializers import (
    CourseSerializer,
    TeacherSerializer,
    ParentSerializer,
    StudentSerializer,
    RegistrarSerializer,
)


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    # permission_classes = [permissions.IsAuthenticated]

class TeacherViewSet(viewsets.ModelViewSet):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()
    permission_classes = [permissions.IsAuthenticated]

class ParentViewSet(viewsets.ModelViewSet):
    serializer_class = ParentSerializer
    queryset = Parent.objects.all()
    permission_classes = [permissions.IsAuthenticated]

class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    permission_classes = [permissions.IsAuthenticated]

class RegistrarViewSet(viewsets.ModelViewSet):
    serializer_class = RegistrarSerializer
    queryset = Registrar.objects.all()
    permission_classes = [permissions.IsAuthenticated]










from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from .models import Course, Teacher, Parent, Student, Registrar, Class, Lesson, Attendance, Payment
from .serializers import *
from account.models import User
from account.api.v1.serializers import RegisterSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [permissions.IsAuthenticated]

class TeacherViewSet(viewsets.ModelViewSet):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()
    permission_classes = [permissions.IsAuthenticated]

class ParentViewSet(viewsets.ModelViewSet):
    serializer_class = ParentSerializer
    queryset = Parent.objects.all()
    permission_classes = [permissions.IsAuthenticated]

class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    permission_classes = [permissions.IsAuthenticated]

class RegistrarViewSet(viewsets.ModelViewSet):
    serializer_class = RegistrarSerializer
    queryset = Registrar.objects.all()
    permission_classes = [permissions.IsAuthenticated]
