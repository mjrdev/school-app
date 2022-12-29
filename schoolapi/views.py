
from rest_framework import viewsets
from schoolapi.models import Student, Course, Teacher, StudentOnCourse
from schoolapi.serialize import StudentSerializer, CourseSerializer, TeacherSerializer, StudentOnCourseSerializer

class StudentsViewSet(viewsets.ModelViewSet):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

class CoursesViewSet(viewsets.ModelViewSet):
  queryset = Course.objects.all()
  serializer_class = CourseSerializer

class TeacherViewSet(viewsets.ModelViewSet):
  queryset = Course.objects.all()
  serializer_class = TeacherSerializer

class StudentOnCourseViewSet(viewsets.ModelViewSet):
  queryset = Course.objects.all()
  serializer_class = CourseSerializer
