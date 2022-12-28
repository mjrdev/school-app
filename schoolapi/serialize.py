from rest_framework import serializers
from schoolapi.models import Student, Course

class StudentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Student
    fields = ['id', 'name', 'cpf']

class CourseSerializer(serializers.ModelSerializer):
  class Meta:
    model = Course
    fields = ['id', 'title', 'description']
