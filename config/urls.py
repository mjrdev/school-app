
from django.contrib import admin
from django.urls import path, include
from schoolapi.views import StudentsViewSet, CoursesViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('students', StudentsViewSet)
router.register('courses', CoursesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('', include(router.urls)),
]
