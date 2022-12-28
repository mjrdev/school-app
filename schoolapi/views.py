
from rest_framework import viewsets
from schoolapi.models import Student
from schoolapi.serialize import StudentSerializer

class StudentsViewSet(viewsets.ModelViewSet):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer