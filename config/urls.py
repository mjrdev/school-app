
from django.contrib import admin
from django.urls import path, include
from schoolapi.views import StudentsViewSet, CoursesViewSet, TeachersViewSet, RegistrationsViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register('students', StudentsViewSet)
router.register('courses', CoursesViewSet)
router.register('teachers', TeachersViewSet)
router.register('registrations', RegistrationsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', include('schoolweb.urls'))
]
