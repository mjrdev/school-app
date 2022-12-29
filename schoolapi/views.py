
from rest_framework import viewsets
from schoolapi.models import Student, Course, Teacher, Registration
from schoolapi.serialize import StudentSerializer, CourseSerializer, TeacherSerializer, RegistrationSerializer

class StudentsViewSet(viewsets.ModelViewSet):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer

class CoursesViewSet(viewsets.ModelViewSet):
  queryset = Course.objects.all()
  serializer_class = CourseSerializer

class TeachersViewSet(viewsets.ModelViewSet):
  queryset = Teacher.objects.all()
  serializer_class = TeacherSerializer

class RegistrationsViewSet(viewsets.ModelViewSet):
  queryset = Registration.objects.all()
  serializer_class = RegistrationSerializer



