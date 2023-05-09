from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from django.http import JsonResponse
from .models import Course, Teacher, Parent, Student, Registrar, Class, Lesson, Attendance, Payment
from .serializers import *
from rest_framework import generics
from rest_framework.response import Response
from account.models import User
from .serializers import  StudentSerializer
from account.api.v1.serializers import RegisterSerializer


class CourseListCreateAPIView(APIView):
    # permission_classes = [permissions.IsAuthenticated]
                                                                                                                               
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return JsonResponse({"data":serializer.data, "soni":courses.count()})

    def post(self, request):
        serializer = CourseSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class CourseRetrieveUpdateDestroyAPIView(APIView):
    # permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        return get_object_or_404(Course, pk=pk)

    def get(self, request, pk):
        course = self.get_object(pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data)

    def put(self, request, pk):
        course = self.get_object(pk)
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        course = self.get_object(pk)
        course.delete()
        return Response(status=204)


class TeacherListCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return JsonResponse({"data":serializer.data, "soni":teachers.count()})

    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class TeacherRetrieveUpdateDestroyAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        return get_object_or_404(Teacher, pk=pk)

    def get(self, request, pk):
        teacher = self.get_object(pk)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)
    
    def put(self, request, pk):
        teacher = self.get_object(pk)
        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        teacher = self.get_object(pk)
        teacher.delete()
        return Response(status=204)


class ParentListCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]    
    def get(self, request):
        parents = Parent.objects.all()
        serializer = ParentSerializer(parents, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ParentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class ParentRetrieveUpdateDestroyAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]    
    def get_object(self, pk):
        return get_object_or_404(Parent, pk=pk)

    def get(self, request, pk):
        parent = self.get_object(pk)
        serializer = ParentSerializer(parent)
        return Response(serializer.data)

    def put(self, request, pk):
        parent = self.get_object(pk)
        serializer = ParentSerializer(parent, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        parent = self.get_object(pk)
        parent.delete()
        return Response(status=204)


class StudentListCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]    
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return JsonResponse({"data":serializer.data, "soni":students.count()})

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class StudentRetrieveUpdateDestroyAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get_object(self, pk):
        return get_object_or_404(Student, pk=pk)

    def get(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        student = self.get_object(pk)
        student.delete()
        return Response(status=204)


class RegistrarListCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]    
    def get(self, request):
        registrars = Registrar.objects.all()
        serializer = RegistrarSerializer(registrars, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RegistrarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)    

class RegistrarRetrieveUpdateDestroyAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]    
    def get_object(self, pk):
        return get_object_or_404(Registrar, pk=pk)

    def get(self, request, pk):
        registrar = self.get_object(pk)
        serializer = RegistrarSerializer(registrar)
        return Response(serializer.data)

    def put(self, request, pk):
        registrar = self.get_object(pk)
        serializer = RegistrarSerializer(registrar, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        registrar = self.get_object(pk)
        registrar.delete()
        return Response(status=204)


class ClassListCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]    
    def get(self, request):
        class_me = Class.objects.all()
        serializer = ClassSerializer(class_me, many=True)
        return JsonResponse({"data":serializer.data, "soni":class_me.count()})

    def post(self, request):
        serializer = ClassSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)    

class ClassRetrieveUpdateDestroyAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]    
    def get_object(self, pk):
        return get_object_or_404(Class, pk=pk)

    def get(self, request, pk):
        class_me = self.get_object(pk)
        serializer = ClassSerializer(class_me)
        return Response(serializer.data)

    def put(self, request, pk):
        class_me = self.get_object(pk)
        serializer = ClassSerializer(class_me, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        class_me = self.get_object(pk)
        class_me.delete()
        return Response(status=204)


class LessonListCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]    
    def get(self, request):
        lesson = Lesson.objects.all()
        serializer = LessonSerializer(lesson, many=True)
        return JsonResponse({"data":serializer.data, "soni":lesson.count()})

    def post(self, request):
        serializer = LessonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)    

class LessonRetrieveUpdateDestroyAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]    
    def get_object(self, pk):
        return get_object_or_404(Class, pk=pk)

    def get(self, request, pk):
        lesson = self.get_object(pk)
        serializer = LessonSerializer(lesson)
        return Response(serializer.data)

    def put(self, request, pk):
        lesson = self.get_object(pk)
        serializer = LessonSerializer(lesson, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        lesson = self.get_object(pk)
        lesson.delete()
        return Response(status=204)


class AttendanceListCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]    
    def get(self, request):
        attendance = Attendance.objects.all()
        serializer = AttendanceSerializer(attendance, many=True)
        return JsonResponse({"data":serializer.data, "soni":attendance.count()})

    def post(self, request):
        serializer = LessonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)    

class AttendanceRetrieveUpdateDestroyAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]    
    def get_object(self, pk):
        return get_object_or_404(Class, pk=pk)

    def get(self, request, pk):
        attendance = self.get_object(pk)
        serializer = AttendanceSerializer(attendance)
        return Response(serializer.data)

    def put(self, request, pk):
        attendance = self.get_object(pk)
        serializer = AttendanceSerializer(attendance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        attendance = self.get_object(pk)
        attendance.delete()
        return Response(status=204)

class PaymentListCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]    
    def get(self, request):
        payment = Payment.objects.all()
        serializer = PaymentSerializer(payment, many=True)
        return JsonResponse({"data":serializer.data, "soni":payment.count()})

    def post(self, request):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)    



class InvoiceListCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]    
    def get(self, request):
        invoices = Invoice.objects.all()
        serializer = InvoiceSerializer(invoices, many=True)
        return JsonResponse({"data":serializer.data, "soni":invoices.count()})

    def post(self, request):
        serializer = InvoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
         
        return Response(serializer.errors, status=400)

class InvoiceRetrieveUpdateDestroyAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]    
    def get_object(self, pk):
        return get_object_or_404(Invoice, pk=pk)

    def get(self, request, pk):
        Invoice = self.get_object(pk)
        serializer = InvoiceSerializer(Invoice)
        return Response(serializer.data)

    def put(self, request, pk):
        Invoice = self.get_object(pk)
        serializer = InvoiceSerializer(Invoice, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        Invoice = self.get_object(pk)
        Invoice.delete()
        return Response(status=204)
    
class LessonScheduleList(generics.ListCreateAPIView):
    queryset = LessonSchedule.objects.all()
    serializer_class = LessonScheduleSerializer

class LessonScheduleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LessonSchedule.objects.all()
    serializer_class = LessonScheduleSerializer


class LessonScheduleCreate(generics.CreateAPIView):
    queryset = LessonSchedule.objects.all()
    serializer_class = LessonScheduleSerializer


class LessonScheduleUpdate(generics.UpdateAPIView):
    queryset = LessonSchedule.objects.all()
    serializer_class = LessonScheduleSerializer
    lookup_field = 'id'