from django.urls import path
from .views import *
from django.urls import path
from .viows2 import *
                    
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('courses', CourseViewSet)
router.register('teachers', TeacherViewSet)
router.register('parents', ParentViewSet)
router.register('students', StudentViewSet)
router.register('registrars', RegistrarViewSet)

urlpatterns = [
    path('', include(router.urls)),
]