from rest_framework import serializers
from schoolapi.models import Student, Course, Teacher, Registration

import string
import random

def generate_code(stringSize, NumberSize):
  return ''.join(random.choice(string.ascii_uppercase) for _ in range(stringSize)) + ''.join(random.choice(string.digits) for _ in range(NumberSize))

class RegistrationSerializer(serializers.ModelSerializer):
  def create(self, validated_data):
    print(validated_data, validated_data['code'])
    validated_data['code'] = generate_code(3, 4)
    return Registration.objects.create(**validated_data)
  class Meta:
    model = Registration
    fields = ['id', 'code', 'student', 'course']

class CourseSerializer(serializers.ModelSerializer):
  registrations = RegistrationSerializer(read_only=True, many=True)

  class Meta:
    model = Course
    fields = ['id', 'shift', 'title', 'description', 'teacher', 'registrations']

class TeacherSerializer(serializers.ModelSerializer):
  courses = CourseSerializer(read_only=True, many=True)
  class Meta:
    model = Teacher
    fields = ['id', 'name', 'cpf', 'email', 'courses']

class StudentSerializer(serializers.ModelSerializer):
  registrations = RegistrationSerializer(read_only=True, many=True)
  class Meta:
    model = Student
    fields = ['id', 'name', 'cpf', 'email', 'registrations']

