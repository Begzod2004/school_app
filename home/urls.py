from django.urls import path
from .views import *
from django.urls import path
from .viows2 import *
                    

urlpatterns = [
    # path('User/', UserListCreateAPIView.as_view(), name='user_list_create'),
    # path('User/<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view(), name='user_retrieve_update_destroy'),

    path('course/', CourseListCreateAPIView.as_view(), name='course_list_create'),
    path('course/<int:pk>/', CourseRetrieveUpdateDestroyAPIView.as_view(), name='course_retrieve_update_destroy'),

    path('teacher/', TeacherListCreateAPIView.as_view(), name='teacher_list_create'),
    path('teacher/<int:pk>/', TeacherRetrieveUpdateDestroyAPIView.as_view(), name='teacher_retrieve_update_destroy'),

    path('parent/', ParentListCreateAPIView.as_view(), name='parent_list_create'),
    path('parent/<int:pk>/', ParentRetrieveUpdateDestroyAPIView.as_view(), name='parent_retrieve_update_destroy'),

    path('student/', StudentListCreateAPIView.as_view(), name='student_list_create'),
    path('student/<int:pk>/', StudentRetrieveUpdateDestroyAPIView.as_view(), name='student_retrieve_update_destroy'),

    path('registrar/', RegistrarListCreateAPIView.as_view(), name='registrar_list_create'),
    path('registrar/<int:pk>/', RegistrarRetrieveUpdateDestroyAPIView.as_view(), name='registrar_retrieve_update_destroy'),

    path('class/', ClassListCreateAPIView.as_view(), name='class_list_create'),
    path('class/<int:pk>/', ClassRetrieveUpdateDestroyAPIView.as_view(), name='class_retrieve_update_destroy'),

    path('lesson/', LessonListCreateAPIView.as_view(), name='lesson_list_create'),
    path('lesson/<int:pk>/', LessonRetrieveUpdateDestroyAPIView.as_view(), name='lesson_retrieve_update_destroy'),

    path('attendance/', AttendanceListCreateAPIView.as_view(), name='attendance_list_create'),
    path('attendance/<int:pk>/', AttendanceRetrieveUpdateDestroyAPIView.as_view(), name='attendance_retrieve_update_destroy'),
   
    path('Invoice/', InvoiceListCreateAPIView.as_view(), name='invoice_list_create'),
    path('Invoice/<int:pk>/', InvoiceRetrieveUpdateDestroyAPIView.as_view(), name='invoice_retrieve_update_destroy'),

    path('payment/', PaymentListCreateAPIView.as_view(), name='attendance_list_create'),

    path('lesson-schedules/', LessonScheduleList.as_view(), name='lessonschedule-list'),
    path('lesson-schedules/<int:pk>/', LessonScheduleDetail.as_view(), name='lessonschedule-detail'),
    path('lessons/update/<int:id>/', LessonScheduleUpdate.as_view(), name='lesson-update'),
    path('lesson-schedules/create/', LessonScheduleCreate.as_view(), name='lesson-create'),
    path('llllllllllllllll/',  payment_list_view)
]
