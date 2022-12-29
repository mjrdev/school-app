from rest_framework import serializers
from schoolapi.models import Student, Course, Teacher, Registration

class StudentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Student
    fields = ['id', 'name', 'cpf', 'email']

class TeacherSerializer(serializers.ModelSerializer):
  class Meta:
    model = Teacher
    fields = ['id', 'name', 'cpf', 'email']

class CourseSerializer(serializers.ModelSerializer):
  class Meta:
    model = Course
    fields = ['id', 'shift', 'title', 'description']

class RegistrationSerializer(serializers.ModelSerializer):
  course_id = CourseSerializer(read_only=True)
  student_id = StudentSerializer(read_only=True)
  class Meta:
    model = Registration
    fields = ['id', 'code', 'course_id', 'student_id']

