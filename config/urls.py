
from django.contrib import admin
from django.urls import path, include
from schoolapi.views import StudentsViewSet, CoursesViewSet, TeacherViewSet, StudentOnCourseViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register('students', StudentsViewSet)
router.register('courses', CoursesViewSet)
router.register('teachers', TeacherViewSet)
router.register('studentsoncourses', StudentOnCourseViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
